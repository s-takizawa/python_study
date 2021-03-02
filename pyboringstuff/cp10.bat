@echo off
setlocal

rem cd /d %~dp0
pushd "%~dp0"

rem 実行
python cp10.py

popd

pause
exit