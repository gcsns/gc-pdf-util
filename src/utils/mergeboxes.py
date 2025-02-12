from typing import List
from logger import logger
from ocrresultwithboxes import OcrResultWithBoxes
from statistics import median, mean
import configs
import csv
import sys

csvwriter = csv.writer(sys.stdout)
class BoundingBox:
    def __init__(self, box, text, score, sourceIndex):
        self.box = box
        self.text = text
        self.score = score
        self.sourceIndex = sourceIndex

    def getBottomY(self) -> float:
        return self.box[3][1]

    def getTopY(self) -> float:
        return self.box[0][1]

    def getStartX(self) -> float:
        return self.box[0][0]

    def getEndX(self) -> float:
        return self.box[1][0]
    
    def getWidth(self) -> float:
        return self.getEndX() - self.getStartX()

    def getCenterX(self) -> float:
        return (self.getStartX() + self.getEndX()) / 2

    def getHeight(self) -> float:
        return self.getBottomY() - self.getTopY()
    
def calculateCloseLineThreshold(sortedYBoxes: List[BoundingBox], pageWidth: int) -> float:
    lineDeltas = []
    csvwriter.writerow(['from box number','from box cordinates', 'from box text', 'to box number', 'to box cordinates', 'to box text, gap'])

    for currentLineIndex in range(0, len(sortedYBoxes)):
        currentLine = sortedYBoxes[currentLineIndex]
        for nextLine in sortedYBoxes[currentLineIndex+1:]:
            allowedAlignmentDiff = pageWidth * configs.LINE_MERGE_CRITERIA_ALLOWED_WIDTH_ALIGNMENT_GAP_PERCENTAGE /100
            if (abs(nextLine.getStartX() - currentLine.getStartX()) >= allowedAlignmentDiff
                    and abs(nextLine.getEndX() - currentLine.getEndX()) >= allowedAlignmentDiff
            ):
                continue

            lineDelta = max(0, nextLine.getTopY() - currentLine.getBottomY())

            # logger.debug(f'gap between box: {previousLine.sourceIndex} and box: {currentLine.sourceIndex} is: {lineDelta}')
            csvwriter.writerow([currentLine.sourceIndex, currentLine.box, currentLine.text, nextLine.sourceIndex, nextLine.box, nextLine.text, lineDelta])
            lineDeltas.append(lineDelta)
            #we need to find exactly 1 nextLine for every currentLine which is aligned
            break

    logger.debug(f'lineDeltas: {sorted(lineDeltas)}')
    if len(lineDeltas) == 0:
        return 0
    deltaMedian = median(lineDeltas)
    logger.debug(f'median: {deltaMedian}')
    adjustedMedian =  deltaMedian * configs.LINE_MERGE_CRITERIA_MEDIAN_PERCENTAGE/100
    logger.debug(f'adjustedMedian: {adjustedMedian}')
    adjustedLineDeltas = []
    for lineDelta in lineDeltas:
        if lineDelta == 0:
            continue
        if lineDelta <= adjustedMedian :
            if (lineDelta % 2) == 0:
                adjustedLineDelta = lineDelta
            else:
                adjustedLineDelta = lineDelta+1
        else:
            continue

        if adjustedLineDelta not in adjustedLineDeltas:
            adjustedLineDeltas.append(adjustedLineDelta)

    adjustedLineDeltas = sorted(adjustedLineDeltas)
    logger.debug(f'adjustedLineDeltas: {adjustedLineDeltas}')
    if not adjustedLineDeltas:
        #empty
        return 0
    else :
        #last element
        return adjustedLineDeltas[-1 if len(adjustedLineDeltas) < configs.LINE_MERGE_CRITERIA_MAX_DELTAS else configs.LINE_MERGE_CRITERIA_MAX_DELTAS - 1 ]


def getCloseBoxPairs(sortedYBoxes: List[BoundingBox], threshold: float, pageWidth: int) -> List[List[BoundingBox]]:
    combinations = []
    lastCombination = None
    for currentLineIndex in range(0, len(sortedYBoxes)):
        currentLine = sortedYBoxes[currentLineIndex]
        for nextLine in sortedYBoxes[currentLineIndex+1:]:
            deltaY = nextLine.getTopY() - currentLine.getBottomY()
            if deltaY > threshold:
                break

            allowedAlignmentDiff = pageWidth * configs.LINE_MERGE_CRITERIA_ALLOWED_WIDTH_ALIGNMENT_GAP_PERCENTAGE /100
            if (abs(currentLine.getStartX() - nextLine.getStartX()) < allowedAlignmentDiff 
                        or abs(currentLine.getEndX() - nextLine.getEndX()) < allowedAlignmentDiff
                ):
                if lastCombination and lastCombination[-1] == currentLine:
                    lastCombination.append(nextLine)
                    logger.debug(f"adding: {nextLine.text} with deltaY: {deltaY} to existing merged box")
                    continue                  
                combination = [currentLine, nextLine]
                combinations.append(combination)
                lastCombination = combination
                logger.debug(f"merging boxes: {combination[0].text} and {combination[1].text} with deltaY: {deltaY}")

    return combinations

def mergeCloseBoxes(ocr_result: OcrResultWithBoxes)->OcrResultWithBoxes:
    if len(ocr_result) == 0:
        return ocr_result
    originalLines = [BoundingBox(ocr_result[index][0], ocr_result[index][1], ocr_result[index][2], index) for index in range(0, len(ocr_result))]
    csvwriter.writerow(['box sequence number', 'cordinates', 'text', 'score'])
    for line in originalLines:
        csvwriter.writerow([line.sourceIndex, line.box, line.text, line.score])
    sortedYLines = sorted(originalLines, key=lambda x: x.getBottomY())
    minStartX = sorted(originalLines, key=lambda x: x.getStartX())[0].getStartX()
    maxEndX = sorted(originalLines, key=lambda x: x.getEndX())[-1].getEndX()
    pageWidth = maxEndX - minStartX
    logger.info(f'pageWidth: {pageWidth}')
    thresholdY = calculateCloseLineThreshold(sortedYLines, pageWidth)
    logger.info(f'thresholdY: {thresholdY}')
    probableBrokenLines = getCloseBoxPairs(sortedYLines, thresholdY, pageWidth)

    mergedBoxes = []
    csvwriter.writerow(['merging boxes as below:'])
    for combination in probableBrokenLines:
        mergedBox = mergeBoxes(combination)
        mergedBoxes.append(mergedBox)

    sortedMergedBoxes = sorted(mergedBoxes, key=lambda x: x.sourceIndex)

    insertedCount = 0
    for mergedBox in sortedMergedBoxes:
        originalLines.insert(mergedBox.sourceIndex + insertedCount, mergedBox )
        insertedCount += 1
    return [ [line.box, line.text, line.score] for line in originalLines]

def mergeBoxes(closeBoxes: list[BoundingBox])-> BoundingBox:
    xMin = min(box.getStartX() for box in closeBoxes)
    xMax = max(box.getEndX() for box in closeBoxes)
    yMin = min(box.getTopY() for box in closeBoxes)
    yMax = max(box.getBottomY() for box in closeBoxes)
    sourceIndex = min(box.sourceIndex for box in closeBoxes)
    csvwriter.writerow([str(box.sourceIndex) for box in closeBoxes])
    return BoundingBox([[xMin,yMin], [xMax, yMin], [xMax, yMax], [xMin, yMax]], " ".join([box.text for box in closeBoxes]), mean(box.score for box in closeBoxes), sourceIndex)
