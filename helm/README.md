# gc-pdf-util

gc-pdf-util is a node-typescript based applications with support for kubernetes

## TL;DR;

```bash
$ helm install gc-pdf-util ./
```

## Introduction

This chart bootstraps a gc-pdf-util cluster deployment on a [Kubernetes](http://kubernetes.io) cluster using the [Helm](https://helm.sh) package manager.

## Prerequisites

- Kubernetes 1.12+
- Helm 2.11+ or Helm 3.0-beta3+
- PV provisioner support in the underlying infrastructure

## Installing the Chart

To install the chart with the release name `gc-pdf-util` from this folder:

```bash
$ helm install gc-pdf-util ./
```

The command deploys gc-pdf-util on the Kubernetes cluster in the default configuration. The [Parameters](#parameters) section lists the parameters that can be configured during installation.

> **Tip**: List all releases using `helm list`

## Uninstalling the Chart

To uninstall/delete the `gc-pdf-util` deployment:

```bash
$ helm delete gc-pdf-util
```

The command removes all the Kubernetes components associated with the chart and deletes the release.

## Parameters

The following table lists the configurable parameters of the gc-pdf-util chart and their default values.

| Parameter          | Description                                                    | Default        |
| ------------------ | -------------------------------------------------------------- | -------------- |
| `image.repository` | gc-pdf-util image name                                         | `gc-pdf-util`  |
| `image.pullPolicy` | Image pull policy                                              | `IfNotPresent` |
| `nameOverride`     | String to override the default fullname template with a string | `gc-pdf-util`  |
| `replicaCount`     | The number of replicas of the core-service to launch           | 1              |

Specify each parameter using the `--set key=value[,key=value]` argument to `helm install`. For example,

```bash
$ helm install my-service \
  --set nameOverride=my-service,replicaCount=3 \
    ./
```

The above command sets the default name prefix to `my-service` and number of replica sets to `3`.

Alternatively, a YAML file that specifies the values for the parameters can be provided while installing the chart. For example,

```bash
$ helm install my-release -f values.yaml ./
```

> **Tip**: You can use the default [values.yaml](values.yaml)
