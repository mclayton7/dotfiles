# Setup prompt
if (($null -ne (Get-Command git -ErrorAction SilentlyContinue)) -and ($null -ne (Get-Module -ListAvailable Oh-My-Posh -ErrorAction SilentlyContinue))) {
    Import-Module Oh-My-Posh
}