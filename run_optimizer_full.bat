@echo off
setlocal

set argument="%2"

set filename=%~1

set output=%filename:txt=json%

"gcsim.exe" -c="%cd%/config/%filename%" -s -substatOptimFull || exit /b %errorlevel%

"gcsim.exe" -c="%cd%/config/%filename%" -out="%cd%/viewer_gz/%output%" -gz="false" %argument%
endlocal
