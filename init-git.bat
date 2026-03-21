@echo off
echo ========================================
echo   百变街舞官网 - Git 初始化脚本
echo ========================================
echo.

cd /d "%~dp0"

echo [1/4] 初始化 Git 仓库...
git init

echo.
echo [2/4] 添加所有文件...
git add .

echo.
echo [3/4] 提交初始版本...
git commit -m "Initial commit - 百变街舞官网 v1.0"

echo.
echo ========================================
echo   下一步操作：
echo ========================================
echo.
echo 1. 在 GitHub 创建新仓库（不要勾选任何选项）
echo    https://github.com/new
echo.
echo 2. 复制仓库地址，然后运行：
echo.
echo    git remote add origin 你的仓库地址
echo    git branch -M main
echo    git push -u origin main
echo.
echo 3. 在 Netlify 添加这个 GitHub 仓库即可自动部署
echo.
echo ========================================
echo.
pause
