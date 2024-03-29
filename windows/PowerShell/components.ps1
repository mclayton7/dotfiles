# These components will be loaded for all PowerShell instances

Push-Location (Join-Path (Split-Path -parent $profile) "components")

# From within the ./components directory...
. .\git.ps1
. .\dotnet.ps1
. .\console.ps1

Pop-Location