import os, sys, base64 as B
C='ZnJvbSByZXF1ZXN0cyBpbXBvcnQgcG9zdCxnZXQKZnJvbSByaWNoLmNvbnNvbGUgaW1wb3J0IENvbnNvbGUKaW1wb3J0IHJlcXVlc3RzLG9zLHJlLHV1aWQKaW1wb3J0IHRpbWUKZnJvbSBjb2xvcmlzdCBpbXBvcnQgQ29sb3IKZnJvbSBjb2xvcmlzdCBpbXBvcnQgcmVkCmZyb20gcmljaC50ZXh0IGltcG9ydCBUZXh0CmZyb20gZGF0ZXRpbWUgaW1wb3J0IGRhdGV0aW1lCmZyb20gY2ZvbnRzIGltcG9ydCByZW5kZXIgCgoKI/CdkI3wnZCI8J2QivCdkJkKIyBNYWRlIEJ5IE5pa3pQeSAKCnVpZD1zdHIodXVpZC51dWlkNCgpKQpjb25zb2xlPUNvbnNvbGUoKQoKZGVmIGhlYWRlcigpOgogICAgb3Muc3lzdGVtKCJjbHMiIGlmIG9zLm5hbWU9PSdudCcgZWxzZSAiY2xlYXIiKQoKCiMgRGVmaW5lIEFOU0kgY29sb3IgY29kZXMgZm9yIHN0eWxpbmcKY2xhc3MgVGV4dENvbG9yOgogICAgSEVBREVSID0gJ1wwMzNbOTBtJyAgIyBNYWdlbnRhCiAgICBPS0JMVUUgPSAnXDAzM1s5N20nICAjIEJsdWUKICAgIE9LQ1lBTiA9ICdcMDMzWzk4bScgICMgQ3lhbgogICAgT0tHUkVFTiA9ICdcMDMzWzk5bScgIyBHcmVlbgogICAgV0FSTklORyA9ICdcMDMzWzk0bScgIyBZZWxsb3cKICAgIEZBSUwgPSAnXDAzM1s4OG0nICAgICMgUmVkCiAgICBFTkRDID0gJ1wwMzNbMG0nICAgICAjIEVuZCBvZiBjb2xvcgogICAgCiAgICAKZGVmIFJlcG9ydF9JbnN0YWdyYW0odGFyZ2V0X2lkLCBzZXNzaW9uaWQsIGNzcmZ0b2tlbik6CiAgICBoZWFkZXIoKQogICAgCiAgICBwcmludChmIntUZXh0Q29sb3IuSEVBREVSfUNob29zZSBSZXBvcnQgVHlwZXtUZXh0Q29sb3IuRU5EQ30iKQogICAgcmVwb3J0X29wdGlvbnMgPSBbCiAgICAgICAgIjEgLSBTcGFtIiwKICAgICAgICAiMiAtIFNlbGYiLAogICAgICAgICIzIC0gRHJ1Z3MiLAogICAgICAgICI0IC0gTnVkaXR5IiwKICAgICAgICAiNSAtIFZpb2xlbmNlIiwKICAgICAgICAiNiAtIEhhdGUiLAogICAgICAgICI3IC0gQnVsbHlpbmciLAogICAgICAgICI4IC0gSW1wZXJzb25hdGlvbiIKICAgIF0KICAgIAogICAgZm9yIG9wdGlvbiBpbiByZXBvcnRfb3B0aW9uczoKICAgICAgICBwcmludChmIiAge1RleHRDb2xvci5PS0NZQU59e29wdGlvbn17VGV4dENvbG9yLkVOREN9IikKCiAgICB3aGlsZSBUcnVlOgogICAgICAgIHRyeToKICAgICAgICAgICAgcmVwb3J0VHlwZSA9IGludChpbnB1dChmIntUZXh0Q29sb3IuT0tHUkVFTn1DaG9vc2U6IHtUZXh0Q29sb3IuRU5EQ30gIikpCiAgICAgICAgICAgIGlmIHJlcG9ydFR5cGUgaW4gcmFuZ2UoMSwgOSk6CiAgICAgICAgICAgICAgICBwcmludChmIntUZXh0Q29sb3IuT0tHUkVFTn1Zb3Ugc2VsZWN0ZWQ6IHtyZXBvcnRUeXBlfXtUZXh0Q29sb3IuRU5EQ30iKQogICAgICAgICAgICAgICAgYnJlYWsKICAgICAgICAgICAgZWxzZToKICAgICAgICAgICAgICAgIHByaW50KGYie1RleHRDb2xvci5GQUlMfUludmFsaWQgaW5wdXQuIFBsZWFzZSBjaG9vc2UgYSBudW1iZXIgYmV0d2VlbiAxIGFuZCA4LntUZXh0Q29sb3IuRU5EQ30iKQogICAgICAgIGV4Y2VwdCBWYWx1ZUVycm9yOgogICAgICAgICAgICBwcmludChmIntUZXh0Q29sb3IuRkFJTH1JbnZhbGlkIGlucHV0LiBQbGVhc2UgZW50ZXIgYSB2YWxpZCBudW1iZXIue1RleHRDb2xvci5FTkRDfSIpCgojIEV4YW1wbGUgY2FsbCB0byB0aGUgZnVuY3Rpb24gKFJlcGxhY2Ugd2l0aCBhY3R1YWwgc2Vzc2lvbiBpbmZvKQojIFJlcG9ydF9JbnN0YWdyYW0oJ3NvbWVfdGFyZ2V0X2lkJywgJ3lvdXJfc2Vzc2lvbl9pZCcsICd5b3VyX2NzcmZfdG9rZW4nKQoKICAgIHdoaWxlIDE6CiAgICAgICAgdHJ5OgogICAgICAgICAgICByMyA9IHBvc3QoCiAgICAgICAgICAgICAgICAiaHR0cHM6Ly9pLmluc3RhZ3JhbS5jb20vdXNlcnMvIiArIHRhcmdldF9pZCArICIvZmxhZy8iLAogICAgICAgICAgICAgICAgaGVhZGVycz17CiAgICAgICAgICAgICAgICAgICAgIlVzZXItQWdlbnQiOiAiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NDsgcnY6MTA5LjApIEdlY2tvLzIwMTAwMTAxIEZpcmVmb3gvMTEwLjAiLAogICAgICAgICAgICAgICAgICAgICJIb3N0IjogImkuaW5zdGFncmFtLmNvbSIsCiAgICAgICAgICAgICAgICAgICAgJ2Nvb2tpZSc6IGYic2Vzc2lvbmlkPXtzZXNzaW9uaWR9IiwKICAgICAgICAgICAgICAgICAgICAiWC1DU1JGVG9rZW4iOiBjc3JmdG9rZW4sCiAgICAgICAgICAgICAgICAgICAgIkNvbnRlbnQtVHlwZSI6ICJhcHBsaWNhdGlvbi94LXd3dy1mb3JtLXVybGVuY29kZWQ7IGNoYXJzZXQ9VVRGLTgiCiAgICAgICAgICAgICAgICB9LAogICAgICAgICAgICAgICAgZGF0YT1mJ3NvdXJjZV9uYW1lPSZyZWFzb25faWQ9e3JlcG9ydFR5cGV9JmZyeF9jb250ZXh0PScsCiAgICAgICAgICAgICAgICBhbGxvd19yZWRpcmVjdHM9RmFsc2UKICAgICAgICAgICAgKSAgICAgICAgIAogICAgICAgICAgICAKICAgICAgICAgICAgaWYgcjMuc3RhdHVzX2NvZGU9PTQyOToKICAgICAgICAgICAgICAgIGNvbnNvbGUucHJpbnQoZiItIEFjY291bnQgRmxhZ2dlZCBbIHtyMy5zdGF0dXNfY29kZX0gXSAiKTtleGl0KCkKICAgICAgICAgICAgZWxpZiByMy5zdGF0dXNfY29kZT09NTAwOgogICAgICAgICAgICAgICAgY29uc29sZS5wcmludChmIi0gVGFyZ2V0IE5vdCBGb3VuZCB3aXRoIHN0YXR1cyBjb2RlIFsge3IzLnN0YXR1c19jb2RlfSBdICIpO2V4aXQoKQogICAgICAgICAgICBlbHNlOgogICAgICAgICAgICAgICAgY29uc29sZS5wcmludChmIlJlcG9ydGQgRG9uZSBbYm9sZCBncmVlbl1zdWNjZXNzZnVsbHlbL2JvbGQgZ3JlZW5dIikgCiAgICAgICAgICAgICAgICB0aW1lLnNsZWVwKDEwKQkJCQkKICAgICAgICBleGNlcHQgcmVxdWVzdHMuZXhjZXB0aW9ucy5Ub29NYW55UmVkaXJlY3RzOgogICAgICAgICAgICBjb25zb2xlLnByaW50KGYiUmVwb3J0ZCBEb25lIFtib2xkIGdyZWVuXXN1Y2Nlc3NmdWxseVsvYm9sZCBncmVlbl0iKSM7ZXhpdCgpCiAgICAgICAgICAgIHRpbWUuc2xlZXAoMTApCiAgICAgICAgZXhjZXB0IEV4Y2VwdGlvbiBhcyBlOgogICAgICAgICAgICBjb25zb2xlLnByaW50KGYiLSBSZXBvcnQgRmFpbGVkIHdpdGggc3RhdHVzIGNvZGUgWyB7cjMuc3RhdHVzX2NvZGV9IF0gIik7ZXhpdCgpCgoKZGVmIHN0YXJ0ZXIoKToKICAgIGNvbnNvbGUucHJpbnQoVGV4dCgiV2VsY29tZSB0byB0aGUgTG9naW4gU3lzdGVtISIsIHN0eWxlPSJib2xkIHVuZGVybGluZSIpKQogICAgCiAgICB1c2VyID0gaW5wdXQoIlwwMzNbMTszMm1FbnRlciBZb3VyIFVzZXJuYW1lIDogXDAzM1swbSIpCiAgICBpZiB1c2VyPT0iIjpjb25zb2xlLnByaW50KCJbIV0gWW91IG11c3Qgd3JpdGUgVGhlIHVzZXIiKTtleGl0KCkKICAgIHBlc3MgPSBpbnB1dCgiXDAzM1sxOzMybSBFbnRlciBZb3VyIFBhc3N3b3JkIDogXDAzM1swbSIpCiAgICBpZiBwZXNzPT0iIjpjb25zb2xlLnByaW50KCJbIV0gWW91IG11c3Qgd3JpdGUgVGhlIHBhc3N3b3JkIik7ZXhpdCgpCiAgICByMT1wb3N0KCdodHRwczovL2kuaW5zdGFncmFtLmNvbS9hcGkvdjEvYWNjb3VudHMvbG9naW4vJyxoZWFkZXJzPXsnVXNlci1BZ2VudCc6ICdJbnN0YWdyYW0gMTE0LjAuMC4zOC4xMjAgQW5kcm9pZCAoMzAvMy4wOyAyMTZkcGk7IDEwODB4MjM0MDsgaHVhd2VpL2dvb2dsZTsgTmV4dXMgNlA7IGFuZ2xlcjsgYW5nbGVyOyBlbl9VUyknLCJBY2NlcHQiOiAiKi8qIiwiQWNjZXB0LUVuY29kaW5nIjogImd6aXAsIGRlZmxhdGUiLCJBY2NlcHQtTGFuZ3VhZ2UiOiAiZW4tVVMiLCJYLUlHLUNhcGFiaWxpdGllcyI6ICIzYnJUdnc9PSIsIlgtSUctQ29ubmVjdGlvbi1UeXBlIjogIldJRkkiLCJDb250ZW50LVR5cGUiOiAiYXBwbGljYXRpb24veC13d3ctZm9ybS11cmxlbmNvZGVkOyBjaGFyc2V0PVVURi04IiwnSG9zdCc6ICdpLmluc3RhZ3JhbS5jb20nfSxkYXRhPXsnX3V1aWQnOiB1aWQsJ3Bhc3N3b3JkJzogcGVzcywndXNlcm5hbWUnOiB1c2VyLCdkZXZpY2VfaWQnOiB1aWQsJ2Zyb21fcmVnJzogJ2ZhbHNlJywnX2NzcmZ0b2tlbic6ICdtaXNzaW5nJywnbG9naW5fYXR0ZW1wdF9jb3VudCc6ICcwJ30sYWxsb3dfcmVkaXJlY3RzPVRydWUpCiAgICBpZiAnbG9nZ2VkX2luX3VzZXInIGluIHIxLnRleHQ6CiAgICAgICAgY29uc29sZS5wcmludCgiTG9nZ2VkIGluIFtib2xkIGdyZWVuXVN1Y2Nlc3NmdWxseVsvYm9sZCBncmVlbl0gIikKICAgICAgICBzZXNzaW9uaWQ9cjEuY29va2llc1snc2Vzc2lvbmlkJ10KICAgICAgICBjc3JmdG9rZW49cjEuY29va2llc1snY3NyZnRva2VuJ10KICAgICAgICB0YXJnZXQ9aW5wdXQoZiJcMDMzWzE7MzZtIFRhcmdldCA6IFwwMzNbMG0gIikgI1RoZSB1c2VybmFtZSBNdXN0IEJlIEVudGVyZWQgTWFudWFsbHkgTm90IENvcHkgJiBQYXN0ZS9uIHQubWUvT19IXzMKCiAgICAgICAgcjI9cG9zdCgnaHR0cHM6Ly9pLmluc3RhZ3JhbS5jb206NDQzL2FwaS92MS91c2Vycy9sb29rdXAvJyxoZWFkZXJzPXsiQ29ubmVjdGlvbiI6ICJjbG9zZSIsICJYLUlHLUNvbm5lY3Rpb24tVHlwZSI6ICJXSUZJIiwibWlkIjoiWE9TSU5nQUJBQUcxSURtYXJhbDNub09venJLMHJyTlNiUHVTYnpIcSIsIlgtSUctQ2FwYWJpbGl0aWVzIjogIjNSND0iLCJBY2NlcHQtTGFuZ3VhZ2UiOiAiYXItc2EiLCJDb250ZW50LVR5cGUiOiAiYXBwbGljYXRpb24veC13d3ctZm9ybS11cmxlbmNvZGVkOyBjaGFyc2V0PVVURi04IiwiVXNlci1BZ2VudCI6ICJJbnN0YWdyYW0gOTkuNC4wIFR3ZWFrUFlfdnYxY2sgKFR3ZWFrUFlfdnYxY2spIiwiQWNjZXB0LUVuY29kaW5nIjogImd6aXAsIGRlZmxhdGUifSxkYXRhPXsic2lnbmVkX2JvZHkiOiAiMzVhMmQ1NDdkM2I2ZmY0MDBmNzEzOTQ4Y2RmZmUwYjc4OWE5MDNmODYxMTdlYjZlMmYzZTU3MzA3OWIyZjAzOC57XCJxXCI6XCIlc1wifSIgJSB0YXJnZXR9KQogICAgICAgIGlmICdObyB1c2VycyBmb3VuZCcgaW4gcjIudGV4dDoKICAgICAgICAgICAgYWR2X3NlYXJjaD1nZXQoZidodHRwczovL3d3dy5pbnN0YWdyYW0uY29tL3t0YXJnZXR9JyxoZWFkZXJzPXsnSG9zdCc6ICd3d3cuaW5zdGFncmFtLmNvbScsJ1VzZXItQWdlbnQnOiAnTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NDsgcnY6MTA5LjApIEdlY2tvLzIwMTAwMTAxIEZpcmVmb3gvMTEwLjAnLCdBY2NlcHQnOiAndGV4dC9odG1sLGFwcGxpY2F0aW9uL3hodG1sK3htbCxhcHBsaWNhdGlvbi94bWw7cT0wLjksaW1hZ2UvYXZpZixpbWFnZS93ZWJwLCovKjtxPTAuOCcsJ0FjY2VwdC1MYW5ndWFnZSc6ICdhcixlbi1VUztxPTAuNyxlbjtxPTAuMycsJ0FjY2VwdC1FbmNvZGluZyc6ICdnemlwLCBkZWZsYXRlLCBicicsJ0Nvbm5lY3Rpb24nOiAna2VlcC1hbGl2ZScsJ0Nvb2tpZSc6IGYnY3NyZnRva2VuPXtjc3JmdG9rZW59JywnVXBncmFkZS1JbnNlY3VyZS1SZXF1ZXN0cyc6ICcxJywnU2VjLUZldGNoLURlc3QnOiAnZG9jdW1lbnQnLCdTZWMtRmV0Y2gtTW9kZSc6ICduYXZpZ2F0ZScsJ1NlYy1GZXRjaC1TaXRlJzogJ25vbmUnLCdTZWMtRmV0Y2gtVXNlcic6ICc/MScsJ1RFJzogJ3RyYWlsZXJzJ30pCiAgICAgICAgICAgIHRyeToKICAgICAgICAgICAgICAgIHRhcmdldF9pZD1yZS5maW5kYWxsKCcicHJvZmlsZV9pZCI6IiguKj8pIicsYWR2X3NlYXJjaC50ZXh0KVswXQogICAgICAgICAgICAgICAgUmVwb3J0X0luc3RhZ3JhbSh0YXJnZXRfaWQsc2Vzc2lvbmlkLGNzcmZ0b2tlbikKICAgICAgICAgICAgZXhjZXB0IEluZGV4RXJyb3I6CiAgICAgICAgICAgICAgICB0cnk6CiAgICAgICAgICAgICAgICAgICAgdGFyZ2V0X2lkPXJlLmZpbmRhbGwoJyJwYWdlX2lkIjoicHJvZmlsZVBhZ2VfKC4qPykiJyxhZHZfc2VhcmNoLnRleHQpWzBdCiAgICAgICAgICAgICAgICAgICAgUmVwb3J0X0luc3RhZ3JhbSh0YXJnZXRfaWQsc2Vzc2lvbmlkLGNzcmZ0b2tlbikKICAgICAgICAgICAgICAgIGV4Y2VwdCBJbmRleEVycm9yOgogICAgICAgICAgICAgICAgICAgIHRyeToKICAgICAgICAgICAgICAgICAgICAgICAgYWR2X3NlYXJjaDI9Z2V0KGYnaHR0cHM6Ly93d3cuaW5zdGFncmFtLmNvbS9hcGkvdjEvdXNlcnMvd2ViX3Byb2ZpbGVfaW5mby8/dXNlcm5hbWU9e3RhcmdldH0nLGhlYWRlcnM9eydIb3N0JzogJ3d3dy5pbnN0YWdyYW0uY29tJywnVXNlci1BZ2VudCc6ICdNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0OyBydjoxMDkuMCkgR2Vja28vMjAxMDAxMDEgRmlyZWZveC8xMTAuMCcsJ0FjY2VwdCc6ICcqLyonLCdBY2NlcHQtTGFuZ3VhZ2UnOiAnYXIsZW4tVVM7cT0wLjcsZW47cT0wLjMnLCdBY2NlcHQtRW5jb2RpbmcnOiAnZ3ppcCwgZGVmbGF0ZSwgYnInLCdYLUNTUkZUb2tlbic6IGNzcmZ0b2tlbiwnWC1JRy1BcHAtSUQnOiAnOTM2NjE5NzQzMzkyNDU5JywnWC1BU0JELUlEJzogJzE5ODM4NycsJ1gtSUctV1dXLUNsYWltJzogJ2htYWMuQVIzS1BFUG9Ya1dZaHd0b0NVS3lVSEs4MEdzRTFnMlBKSTF1UHREbEN5bzRQSEtuJywnWC1SZXF1ZXN0ZWQtV2l0aCc6ICdYTUxIdHRwUmVxdWVzdCcsJ0FsdC1Vc2VkJzogJ3d3dy5pbnN0YWdyYW0uY29tJywnQ29ubmVjdGlvbic6ICdrZWVwLWFsaXZlJywnUmVmZXJlcic6IGYnaHR0cHM6Ly93d3cuaW5zdGFncmFtLmNvbS97dGFyZ2V0fS8nLCdDb29raWUnOiAgZidzZXNzaW9uaWQ9e3Nlc3Npb25pZH0nLCdTZWMtRmV0Y2gtRGVzdCc6ICdlbXB0eScsJ1NlYy1GZXRjaC1Nb2RlJzogJ2NvcnMnLCdTZWMtRmV0Y2gtU2l0ZSc6ICdzYW1lLW9yaWdpbicsJ1RFJzogJ3RyYWlsZXJzJ30pCiAgICAgICAgICAgICAgICAgICAgICAgIHRhcmdldF9pZD1hZHZfc2VhcmNoMi5qc29uKClbJ2RhdGEnXVsndXNlciddWydpZCddCiAgICAgICAgICAgICAgICAgICAgICAgIFJlcG9ydF9JbnN0YWdyYW0odGFyZ2V0X2lkLHNlc3Npb25pZCxjc3JmdG9rZW4pCiAgICAgICAgICAgICAgICAgICAgZXhjZXB0IEtleUVycm9yOgogICAgICAgICAgICAgICAgICAgICAgICBjb25zb2xlLnByaW50KCdcbi0gW2JvbGQgcmVkXUZhaWxlZFsvYm9sZCByZWRdIHRvIGdldCB0YXJnZXQgdXNlcm5hbWUsIFRyeSBlbnRlcmluZyB0aGUgVGFyZ2V0IElEIG1hbnVhbGx5IC5cbicpCiAgICAgICAgICAgICAgICAgICAgICAgIHRhcmdldF9pZD1pbnB1dCgnLSBFbnRlciBUaGUgVGFyZ2V0IElEIDogJykKICAgICAgICAgICAgICAgICAgICAgICAgUmVwb3J0X0luc3RhZ3JhbSh0YXJnZXRfaWQsc2Vzc2lvbmlkLGNzcmZ0b2tlbikKICAgICAgICBlbGlmICcic3BhbSI6dHJ1ZScgaW4gcjIudGV4dDoKICAgICAgICAgICAgY29uc29sZS5wcmludCgiLSBUcnkgYWdhaW4gTGF0ZXIgISIpO2V4aXQoKQogICAgICAgIGVsc2U6CiAgICAgICAgICAgIHRyeToKICAgICAgICAgICAgICAgIHRhcmdldF9pZD1zdHIocjIuanNvbigpWyd1c2VyX2lkJ10pCiAgICAgICAgICAgICAgICBSZXBvcnRfSW5zdGFncmFtKHRhcmdldF9pZCxzZXNzaW9uaWQsY3NyZnRva2VuKQogICAgICAgICAgICBleGNlcHQgS2V5RXJyb3I6CiAgICAgICAgICAgICAgICBjb25zb2xlLnByaW50KCctIEdlbmVyYWwgW2JvbGQgcmVkXUVycm9yWy9ib2xkIHJlZF0gLi4uJyk7ZXhpdCgpIAojTmlrelB5CiAgICBlbGlmICdpcF9ibG9jaycgaW4gcjEudGV4dDoKICAgICAgICBjb25zb2xlLnByaW50KCItIFlvdSBIYXZlIFtib2xkIHJlZF1iYW5uZWRbL2JvbGQgcmVkXSBmcm9tIEluc3RhZ3JhbSAoIFtib2xkIHJlZF1pcCBibG9ja1svYm9sZCByZWRdICkgISIpO2V4aXQoKQogICAgZWxpZiAnVGhlIHBhc3N3b3JkIHlvdSBlbnRlcmVkIGlzIGluY29ycmVjdCcgaW4gcjEudGV4dDoKICAgICAgICBjb25zb2xlLnByaW50KCItIFBsZWFzZSBjaGVjayBZb3VyIFBhc3N3b3JkICEiKTtleGl0KCkKICAgIGVsaWYgIlBsZWFzZSBjaGVjayB5b3VyIHVzZXJuYW1lIGFuZCB0cnkgYWdhaW4uIiBpbiByMS50ZXh0OgogICAgICAgIGNvbnNvbGUucHJpbnQoIi0gdXNlcm5hbWUgTm90IEZvdW5kICEiKTtleGl0KCkKICAgIGVsaWYgJ3R3b19mYWN0b3JfcmVxdWlyZWQnIGluIHIxLnRleHQ6CiAgICAgICAgY29uc29sZS5wcmludCgiLSBbYm9sZCBvcmFuZ2UzXVR3byBGYWN0b3JbL2JvbGQgb3JhbmdlM10gISAuLi4iKTtleGl0KCkKICAgIGVsaWYgJ2NoYWxsZW5nZV9yZXF1aXJlZCcgaW4gcjEudGV4dDoKICAgICAgICBjb25zb2xlLnByaW50KCItIFtib2xkIG9yYW5nZTNdU2VjdXJlWy9ib2xkIG9yYW5nZTNdIEFjY291bnQgISAuLi4iKTtleGl0KCkKICAgIGVsaWYgJ2luYWN0aXZlIHVzZXInIGluIHIxLnRleHQ6CiAgICAgICAgY29uc29sZS5wcmludCgnLSBUaGlzIHVzZXIgaXMgW2JvbGQgcmVkXWJhbm5lZFsvYm9sZCByZWRdIGZyb20gSW5zdGFncmFtIC4uLicpO2V4aXQoKQogICAgZWxpZiAiV2UncmUgd29ya2luZyBvbiBpdCBhbmQgd2UnbGwgZ2V0IGl0IGZpeGVkIGFzIHNvb24gYXMgd2UgY2FuLiIgaW4gcjEudGV4dDoKICAgICAgICBjb25zb2xlLnByaW50KCItIFRyeSBhZ2FpbiBpbiBhIG1pbnV0ZSAhIik7ZXhpdCgpCiAgICBlbGlmICdQbGVhc2Ugd2FpdCBhIGZldyBtaW51dGVzIGJlZm9yZSB5b3UgdHJ5IGFnYWluJyBpbiByMS50ZXh0OgogICAgICAgIGNvbnNvbGUucHJpbnQoIi0gVHJ5IGFnYWluIGluIGEgbWludXRlICEiKTtleGl0KCkKICAgIGVsaWYgJ0JhZCByZXF1ZXN0JyBpbiByMS50ZXh0OgogICAgICAgIGNvbnNvbGUucHJpbnQoIi0gW2JvbGQgcmVkXUVycm9yWy9ib2xkIHJlZF0gaW4gaW5zdGFncmFtLCB0cnkgYWdhaW4gaW4gMTUgbWludXRlcyAuLi4iKTtleGl0KCkKICAgIGVsaWYgJ0ludmFsaWQgUGFyYW1ldGVycycgaW4gcjEudGV4dDoKICAgICAgICBjb25zb2xlLnByaW50KCItIFtib2xkIHJlZF1FcnJvclsvYm9sZCByZWRdIFBsZWFzZSBSZWluc3RhbGwgVGhlIFRvb2wgRnJvbSBUaGUgb3JpZ2luYWwgU291cmNlIC4uLiAiKTtleGl0KCkKICAgIGVsc2U6CiAgICAgICAgY29uc29sZS5wcmludCgnLSBHZW5lcmFsIFtib2xkIHJlZF1FcnJvclsvYm9sZCByZWRdIC4uLicpO2V4aXQoKSAgICAKCgojTmlrelB5CmhlYWRlcigpO3N0YXJ0ZXIoKQ=='
exec(B.b64decode(C).decode('utf-8'))
