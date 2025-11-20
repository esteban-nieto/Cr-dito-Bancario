@echo off
echo Subiendo cambios a GitHub...
git add .
git commit -m "Actualización automática %date% %time%"
git push
echo Listo ✅
pause


'''
.\push.bat
'''