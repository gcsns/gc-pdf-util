{{/* vim: set filetype=mustache: */}}

{{- define "helm-toolkit.utils.joinListWithComma" -}}
{{- $local := dict "first" true -}}
{{- range $k, $v := . -}}{{- if not $local.first -}},{{- end -}}{{- $v -}}{{- $_ := set $local "first" false -}}{{- end -}}
{{- end -}}

{{/* Expand the name of the chart. */}}
{{- define "gc-pdf-util.name" -}}
{{- default .Chart.Name .Values.nameOverride | replace "+" "_" | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{/* Set the default version to helm version if no override is provided. */}}
{{- define "gc-pdf-util.version" -}}
{{- default .Chart.AppVersion .Values.image.versionOverride -}}
{{- end -}}

{{/* Create chart name and version as used by the chart label. */}}
{{- define "gc-pdf-util.chart" -}}
{{- printf "%s-%s" .Chart.Name .Chart.Version | replace "+" "_" | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{- define "gc-pdf-util.certificateIssuer" -}}
{{ if eq (lower .Values.certificates.issuer) "external" }}{{ .Values.certificates.externalIssuerName }}{{ else }}{{ include "gc-pdf-util.name" . }}-issuer{{ end }}
{{- end -}}

{{/* Common labels */}}
{{- define "gc-pdf-util.labels" -}}
helm.sh/chart: {{ include "gc-pdf-util.chart" . }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
app.kubernetes.io/version: {{ include "gc-pdf-util.version" . }}
app.kubernetes.io/copyright: "GamechangeSolutions"
app.kubernetes.io/author: "Gamechange"

app.kubernetes.io/name: {{ include "gc-pdf-util.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end -}}

{{/* Selector labels for core */}}
{{- define "gc-pdf-util.coreSelectorLabels" -}}
app.kubernetes.io/component: "{{ include "gc-pdf-util.name" . }}-core"
{{- end -}}

{{/* Docker config json */}}
{{- define "gc-pdf-util.docker-config" -}}
{{ if .Files.Glob "auth.docker.json" }}{{ .Files.Get "auth.docker.json" | b64enc }}
{{- else }}{{- printf "{ \"auths\": { \"https://index.docker.io/v1/\": { \"auth\": \"%s\" } } }" (printf "%s:%s" .Values.image.hubCredentials.username .Values.image.hubCredentials.password | b64enc) | b64enc }}{{- end }}
{{- end -}}

{{/* Pull secrets */}}
{{- define "gc-pdf-util.pull-secrets" -}}
{{ if .Values.image.pullSecrets }}
{{- toYaml .Values.image.pullSecrets }}
{{- end -}}
{{ if .Values.image.fromGcHub }}
- name: {{ include "gc-pdf-util.name" . }}-docker-config
{{- end -}}
{{- end -}}