
{{/* vim: set filetype=mustache: */}}
{{- define "cryptocurrency-price-fetcher.name" -}}
  {{- default "cryptocurrency-price-fetcher" .Values.nameOverride | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{- define "cryptocurrency-price-fetcher.fullname" -}}
  {{- default .Release.Name .Values.fullnameOverride | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{- define "cryptocurrency-price-fetcher.chart" -}}
  {{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" -}}
{{- end -}}
