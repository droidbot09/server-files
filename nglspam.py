import base64
exec(base64.b64decode('W1wb3J0IGpzb24KaW1wb3J0IHJhbmRvbQppbXBvcnQgdGltZQppbXBvcnQgaHR0cHgKaW1wb3J0IHN5cwppbXBvcnQgb3MKaW1wb3J0IHRocmVhZGluZwpmcm9tIGNvbmN1cnJlbnQuZnV0dXJlcyBpbXBvcnQgVGhyZWFkUG9vbEV4ZWN1dG9yCmZyb20gY29sb3JhbWEgaW1wb3J0IEZvcmUsIFN0eWxlLCBpbml0CmltcG9ydCBiYW5uZXIKZnJvbSBtc2cgaW1wb3J0IHJhbmRvbVF1ZXN0aW9ucwoKIyBJbml0aWFsaXplIGNvbG9yYW1hCmluaXQoKQoKc2VudCwgZXJyb3JlZCA9IDAsIDAKCmRlc2NyaXB0aW9uID0gZiIiIgp7Rm9yZS5NQUdFTlRBICsgU3R5bGUuQlJJR0hUffCfmoAgTkdMIE1lc3NhZ2UgU2VuZGVyIPCfmoAKe1N0eWxlLlJFU0VUX0FMTH0tLS0tLS0tLS0tLS0tLS0tLS0Ke0ZvcmUuUkVTRVQgKyBTdHlsZS5CUklHSFR9VGhpcyBzY3JpcHQgaXMgZGVzaWduZWQgdG8gYXV0b21hdGUgdGhlIHByb2Nlc3Mgb2Ygc2VuZGluZyBtZXNzYWdlcyB0byBhIHVzZXIncyBOR0wgbGluay4KSXQgc3VwcG9ydHMgc2VuZGluZyBtZXNzYWdlcyBjb25jdXJyZW50bHkgdXNpbmcgbXVsdGlwbGUgdGhyZWFkcyBhbmQgY2FuIGJlIGNvbmZpZ3VyZWQKdG8gdXNlIHByb3hpZXMgYW5kIHJhbmRvbSBtZXNzYWdlcy4KCkNyZWF0ZWQgYnk6IHtGb3JlLkNZQU4gKyBTdHlsZS5CUklHSFR98J+RqOKAjfCfkrsgSGFja2luZzA5MTIKR2l0SHViIFJlcG9zaXRvcnk6IHtGb3JlLlJFU0VUICsgU3R5bGUuQlJJR0hUffCflJcgaHR0cHM6Ly9naXRodWIuY29tL0hhY2tpbmcwOTEyL25nbC1tc2QKe0ZvcmUuQkxVRSArIFN0eWxlLkJSSUdIVH1QbGVhc2Ugc3RhciB0aGUgcmVwb3NpdG9yeSBpZiB5b3UgZmluZCB0aGlzIHNjcmlwdCB1c2VmdWwuCgp7Rm9yZS5ZRUxMT1cgKyBTdHlsZS5CUklHSFR94pqg77iPIERJU0NMQUlNRVI6IFRoaXMgc2NyaXB0IGlzIGZvciBlZHVjYXRpb25hbCBwdXJwb3NlcyBvbmx5LiBEbyBub3QgdXNlIGl0IGZvciBzcGFtbWluZyBvciBhbnkgZm9ybSBvZiBoYXJhc3NtZW50LiDimqDvuI97U3R5bGUuUkVTRVRfQUxMfQoiIiIKCmNsYXNzIENvbnNvbGU6CiAgICBsb2NrID0gdGhyZWFkaW5nLkxvY2soKQoKICAgIEBzdGF0aWNtZXRob2QKICAgIGRlZiBnZXRfdGltZSgpIC0+IHN0cjoKICAgICAgICByZXR1cm4gdGltZS5zdHJmdGltZSgiJUg6JU06JVMiLCB0aW1lLmdtdGltZSgpKQoKICAgIEBzdGF0aWNtZXRob2QKICAgIGRlZiBsb2dnZXIoc2VudDogaW50LCBlcnJvcmVkOiBpbnQsIG1lc3NhZ2U9IiIsIHZlcmJvc2U9RmFsc2UpIC0+IE5vbmU6CiAgICAgICAgd2l0aCBDb25zb2xlLmxvY2s6CiAgICAgICAgICAgIGxvZ19tZXNzYWdlID0gZidbe0NvbnNvbGUuZ2V0X3RpbWUoKX1dIHttZXNzYWdlfScgICMgRGVmaW5lIGxvZ19tZXNzYWdlIGhlcmUKICAgICAgICAgICAgaWYgdmVyYm9zZToKICAgICAgICAgICAgICAgIHByaW50KGYne0ZvcmUuQ1lBTiArIFN0eWxlLkJSSUdIVH1bVkVSQk9TRV17U3R5bGUuUkVTRVRfQUxMfSB7U3R5bGUuQlJJR0hUfXtsb2dfbWVzc2FnZX0nKQogICAgICAgICAgICBlbHNlOgogICAgICAgICAgICAgICAgc3lzLnN0ZG91dC53cml0ZSgKICAgICAgICAgICAgICAgICAgICBmJ1xye1N0eWxlLkJSSUdIVCArIEZvcmUuR1JFRU59U2VudCB7U3R5bGUuQlJJR0hUICsgRm9yZS5ZRUxMT1d9e3NlbnR9e1N0eWxlLkJSSUdIVCArIEZvcmUuR1JFRU59IG1lc3NhZ2VzLCB7U3R5bGUuQlJJR0hUICsgRm9yZS5SRUR9RXJyb3JlZCB7U3R5bGUuQlJJR0hUICsgRm9yZS5ZRUxMT1d9e2Vycm9yZWR9e1N0eWxlLkJSSUdIVCArIEZvcmUuR1JFRU59IG1lc3NhZ2Vze1N0eWxlLlJFU0VUX0FMTH0nKQogICAgICAgICAgICAgICAgc3lzLnN0ZG91dC5mbHVzaCgpCgogICAgQHN0YXRpY21ldGhvZAogICAgZGVmIGNsZWFyKCkgLT4gTm9uZToKICAgICAgICBvcy5zeXN0ZW0oImNscyIgaWYgb3MubmFtZSA9PSAibnQiIGVsc2UgImNsZWFyIikKCmRlZiBtYWluKHVzZXJuYW1lLCBtZXNzYWdlLCBkZXZpY2VpZCwgcHJveHksIHByb3h5c3RhdHVzLCB2ZXJib3NlLCBtZXNzYWdlX2lucHV0KToKICAgIGdsb2JhbCBlcnJvcmVkCiAgICBnbG9iYWwgc2VudAoKICAgIGlmIG1lc3NhZ2VfaW5wdXQubG93ZXIoKSAhPSAncmFuZG9tJzoKICAgICAgICAjIElmIHRoZSB1c2VyIHByb3ZpZGVkIGEgc3BlY2lmaWMgbWVzc2FnZSwgdXNlIHRoYXQgbWVzc2FnZQogICAgICAgIG1lc3NhZ2UgPSBtZXNzYWdlX2lucHV0CgogICAgaGVhZGVycyA9IHsKICAgICAgICAiQ29udGVudC1UeXBlIjogImFwcGxpY2F0aW9uL3gtd3d3LWZvcm0tdXJsZW5jb2RlZCIsCiAgICAgICAgIkFjY2VwdC1MYW5ndWFnZSI6ICJlbi1VUyxlbjtxPTAuNSIsCiAgICAgICAgIkFjY2VwdCI6ICJ0ZXh0L2h0bWwsYXBwbGljYXRpb24veGh0bWwreG1sLGFwcGxpY2F0aW9uL3htbDtxPTAuOSxpbWFnZS9hdmlmLGltYWdlL3dlYnAsKi8qO3E9MC44IiwKICAgICAgICAiVXNlci1BZ2VudCI6ICJNb3ppbGxhLzUuMCAoWDExOyBVYnVudHU7IExpbnV4IHg4Nl82NDsgcnY6MTA0LjApIEdlY2tvLzIwMTAwMTAxIEZpcmVmb3gvMTA0LjAiLAogICAgfQoKICAgIGlmIHByb3h5c3RhdHVzOgogICAgICAgIGNsaWVudCA9IGh0dHB4LkNsaWVudChoZWFkZXJzPWhlYWRlcnMsIHByb3hpZXM9cHJveHkpCiAgICBlbHNlOgogICAgICAgIGNsaWVudCA9IGh0dHB4LkNsaWVudChoZWFkZXJzPWhlYWRlcnMpCgogICAgdHJ5OgogICAgICAgIGlmIG1lc3NhZ2VfaW5wdXQubG93ZXIoKSA9PSAncmFuZG9tJzoKICAgICAgICAgICAgbWVzc2FnZSA9IG1lc3NhZ2VzKCkgICMgVXNlIHJhbmRvbSBtZXNzYWdlIHdoZW4gbWVzc2FnZV9pbnB1dCBpcyAncmFuZG9tJwoKICAgICAgICBwb3N0cmVzcCA9IGNsaWVudC5wb3N0KAogICAgICAgICAgICBmImh0dHBzOi8vbmdsLmxpbmsvYXBpL3N1Ym1pdCIsCiAgICAgICAgICAgIGRhdGE9ewogICAgICAgICAgICAgICAgInVzZXJuYW1lIjogdXNlcm5hbWUsCiAgICAgICAgICAgICAgICAicXVlc3Rpb24iOiBtZXNzYWdlLAogICAgICAgICAgICAgICAgImRldmljZUlkIjogZGV2aWNlaWQsCiAgICAgICAgICAgIH0sCiAgICAgICAgKQoKICAgICAgICBpZiBwb3N0cmVzcC5zdGF0dXNfY29kZSA9PSAyMDA6CiAgICAgICAgICAgIHNlbnQgKz0gMQogICAgICAgICAgICBDb25zb2xlLmxvZ2dlcihzZW50LCBlcnJvcmVkLCBmJ3tGb3JlLkdSRUVOICsgU3R5bGUuQlJJR0hUfVsrXSBNZXNzYWdlIHN1Y2Nlc3NmdWxseSBzZW50IHRvIHt1c2VybmFtZX06IHtTdHlsZS5SRVNFVF9BTEx9e0ZvcmUuQkxVRSArIFN0eWxlLkJSSUdIVH17bWVzc2FnZX17U3R5bGUuUkVTRVRfQUxMfScsIHZlcmJvc2UpCgogICAgICAgICAgICAjIExvZyB0aGUgc2VudCBtZXNzYWdlIHRvIGEgZmlsZQogICAgICAgICAgICB3aXRoIG9wZW4oInNlbnRfbWVzc2FnZXMubG9nIiwgImEiKSBhcyBsb2dfZmlsZToKICAgICAgICAgICAgICAgIGxvZ19maWxlLndyaXRlKGYiW3tDb25zb2xlLmdldF90aW1lKCl9XSBTZW50IG1lc3NhZ2UgdG8ge3VzZXJuYW1lfToge21lc3NhZ2V9XG4iKQoKICAgICAgICBlbGlmIHBvc3RyZXNwLnN0YXR1c19jb2RlID09IDQwNDoKICAgICAgICAgICAgZXJyb3JlZCArPSAxCiAgICAgICAgICAgIENvbnNvbGUubG9nZ2VyKHNlbnQsIGVycm9yZWQsIGYne0ZvcmUuUkVEICsgU3R5bGUuQlJJR0hUfVsrXSBVc2VyIHt1c2VybmFtZX0gZG9lcyBub3QgZXhpc3R7U3R5bGUuUkVTRVRfQUxMfScsIHZlcmJvc2UpCiAgICAgICAgICAgIGV4aXQoKQogICAgICAgIGVsaWYgcG9zdHJlc3Auc3RhdHVzX2NvZGUgPT0gNDI5OgogICAgICAgICAgICBlcnJvcmVkICs9IDEKICAgICAgICAgICAgQ29uc29sZS5sb2dnZXIoc2VudCwgZXJyb3JlZCwgZid7Rm9yZS5SRUQgKyBTdHlsZS5CUklHSFR9WytdIFVzZXIge3VzZXJuYW1lfSBpcyByYXRlIGxpbWl0ZWR7U3R5bGUuUkVTRVRfQUxMfScsIHZlcmJvc2UpCiAgICAgICAgZWxzZToKICAgICAgICAgICAgZXJyb3JlZCArPSAxCiAgICAgICAgICAgIENvbnNvbGUubG9nZ2VyKHNlbnQsIGVycm9yZWQsIGYne0ZvcmUuUkVEICsgU3R5bGUuQlJJR0hUfVsrXSBFcnJvciB7cG9zdHJlc3Auc3RhdHVzX2NvZGV9IHdoaWxlIHNlbmRpbmcgbWVzc2FnZSB0byB7dXNlcm5hbWV9e1N0eWxlLlJFU0VUX0FMTH0nLCB2ZXJib3NlKQoKICAgIGV4Y2VwdCBFeGNlcHRpb24gYXMgZToKICAgICAgICBlcnJvcmVkICs9IDEKICAgICAgICBDb25zb2xlLmxvZ2dlcihzZW50LCBlcnJvcmVkLCBmJ3tGb3JlLlJFRCArIFN0eWxlLkJSSUdIVH1bK10gRXJyb3I6IHtlfSB3aGlsZSBzZW5kaW5nIG1lc3NhZ2UgdG8ge3VzZXJuYW1lfXtTdHlsZS5SRVNFVF9BTEx9JywgdmVyYm9zZSkKCmRlZiBtZXNzYWdlcygpOgogICAgcmV0dXJuIHJhbmRvbS5jaG9pY2UocmFuZG9tUXVlc3Rpb25zKQoKZGVmIHByb3h5KCk6CiAgICByZXR1cm4gImh0dHA6Ly8iICsgcmFuZG9tLmNob2ljZShsaXN0KG9wZW4oInByb3h5LnR4dCIpKSkKCmRlZiBkZXZpY2VpZCgpOgogICAgcmV0dXJuICIiLmpvaW4ocmFuZG9tLmNob2ljZSgiMDEyMzQ1Njc4OWFiY2RlZmdoaWprbG1ub3BxcnN0dXZ3eHl6LSIpIGZvciBfIGluIHJhbmdlKDM2KSkKCmRlZiBoYW5kbGVyKCk6CiAgICBDb25zb2xlLmNsZWFyKCkKICAgIHByaW50KGJhbm5lci5iYW5uZXIpCiAgICBwcmludChkZXNjcmlwdGlvbikKICAgIHVzZXJuYW1lID0gc3RyKGlucHV0KGYie0ZvcmUuQ1lBTiArIFN0eWxlLkJSSUdIVH1FbnRlciB1c2VybmFtZSAoQWxvbmcgd2l0aCBudW1iZXJzIGluIHRoZWlyIE5HTCBsaW5rKToge1N0eWxlLlJFU0VUX0FMTH0iICsgU3R5bGUuQlJJR0hUKSkKICAgIHRocmVhZGNvdW50ID0gaW50KGlucHV0KGYie0ZvcmUuQ1lBTiArIFN0eWxlLkJSSUdIVH1FbnRlciB0aHJlYWQgY291bnQgKHRoZSBudW1iZXIgb2YgbWVzc2FnZXMgZXg6IDEtMTAwKToge1N0eWxlLlJFU0VUX0FMTH0iICsgU3R5bGUuQlJJR0hUKSkKICAgIG1lc3NhZ2VfaW5wdXQgPSBzdHIoaW5wdXQoZiJ7Rm9yZS5DWUFOICsgU3R5bGUuQlJJR0hUfUVudGVyIG1lc3NhZ2UgKHR5cGUgJ3JhbmRvbScgZm9yIHJhbmRvbSBtZXNzYWdlcyk6IHtTdHlsZS5SRVNFVF9BTEx9IiArIFN0eWxlLkJSSUdIVCkpCgogICAgc3RhcnRfdGltZSA9IHRpbWUudGltZSgpICAjIFJlY29yZCB0aGUgc3RhcnQgdGltZQogICAgCiAgICB3aXRoIG9wZW4oImNvbmZpZy5qc29uIikgYXMgY29uZmlnX2ZpbGU6CiAgICAgICAgY29uZmlnX2RhdGEgPSBqc29uLmxvYWQoY29uZmlnX2ZpbGUpCiAgICAgICAgcHJveHlzdGF0dXMgPSBjb25maWdfZGF0YS5nZXQoInByb3h5IiwgRmFsc2UpCiAgICAgICAgZGVsYXkgPSBjb25maWdfZGF0YS5nZXQoImRlbGF5IiwgMCkKICAgICAgICB2ZXJib3NlID0gY29uZmlnX2RhdGEuZ2V0KCJ2ZXJib3NlIiwgRmFsc2UpCiAgICAgICAgcHJpbnQoZidcbntGb3JlLk1BR0VOVEEgKyBTdHlsZS5CUklHSFR98J+agCBBdHRhY2tpbmcgU3RhcnRlZCDwn5qAIHtTdHlsZS5SRVNFVF9BTEx9JykKICAgICAgICBwcmludCgnLS0tLS0tLS0tLS0tLS0tLS0tXG4nKQoKICAgIHdpdGggVGhyZWFkUG9vbEV4ZWN1dG9yKG1heF93b3JrZXJzPXRocmVhZGNvdW50KSBhcyBleGVjdXRvcjoKICAgICAgICBmb3IgXyBpbiByYW5nZSh0aHJlYWRjb3VudCk6CiAgICAgICAgICAgIGV4ZWN1dG9yLnN1Ym1pdChtYWluLCB1c2VybmFtZSwgbWVzc2FnZV9pbnB1dCwgZGV2aWNlaWQoKSwgcHJveHkoKSwgcHJveHlzdGF0dXMsIHZlcmJvc2UsIG1lc3NhZ2VfaW5wdXQpCiAgICAgICAgICAgIHRpbWUuc2xlZXAoZGVsYXkpCgogICAgZWxhcHNlZF90aW1lID0gdGltZS50aW1lKCkgLSBzdGFydF90aW1lICAjIENhbGN1bGF0ZSB0aGUgZWxhcHNlZCB0aW1lCiAgICBDb25zb2xlLmxvZ2dlcihzZW50LCBlcnJvcmVkKQogICAgcHJpbnQoZidcblxue0ZvcmUuTUFHRU5UQSArIFN0eWxlLkJSSUdIVH3wn46JIEF0dGFjayBDb21wbGV0ZWQgaW4ge2VsYXBzZWRfdGltZTouMmZ9IHNlY29uZHMg8J+OiSB7U3R5bGUuUkVTRVRfQUxMfVxuJykKCmlmIF9fbmFtZV9fID09ICJfX21haW5fXyI6CiAgICBoYW5kbGVyKCk=').decode('utf-8'))
