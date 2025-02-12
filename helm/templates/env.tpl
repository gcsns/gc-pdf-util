{{- define "gc-pdf-util.default-env-config" -}}
- name: AUTH_SERVER_ISSUER
  valueFrom:
    configMapKeyRef:
      name: {{ include "gc-pdf-util.name" . }}-environment
      key: AUTH_SERVER_ISSUER
- name: AUTH_SERVER_AUDIENCE
  valueFrom:
    configMapKeyRef:
      name: {{ include "gc-pdf-util.name" . }}-environment
      key: AUTH_SERVER_AUDIENCE
- name: AUTH_SERVER_BASE_URL
  valueFrom:
    configMapKeyRef:
      name: {{ include "gc-pdf-util.name" . }}-environment
      key: AUTH_SERVER_BASE_URL
{{- range $k, $v := .Values.additionalEnvConfig }}
- name: {{ $k }}
  valueFrom:
    configMapKeyRef:
      name: {{ include "gc-pdf-util.name" $ }}-environment
      key: {{ $k }}
{{- end }}

{{- range $k, $v := .Values.additionalEnvSecret }}
- name: {{ $k }}
  valueFrom:
    secretKeyRef:
      name: {{ include "gc-pdf-util.name" $ }}-secret
      key: {{ $k }}
{{- end }}
{{- end -}}
