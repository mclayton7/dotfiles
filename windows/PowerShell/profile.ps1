# Profile for the Microsoft.Powershell Shell, only. (Not Visual Studio or other PoSh instances)
# ===========

# Source other pieces
Push-Location (Split-Path -parent $profile)
"components", "functions", "aliases", "exports", "extra" | Where-Object { Test-Path "$_.ps1" } | ForEach-Object -process { Invoke-Expression ". .\$_.ps1" }
Pop-Location

function Prompt {
	Update-NavigationHistory $pwd.Path
}

# https://ohmyposh.dev/docs/git
$env:POSH_GIT_ENABLED = $true

Import-Module Terminal-Icons
Import-Module posh-git
Import-Module oh-my-posh

# https://www.hanselman.com/blog/you-should-be-customizing-your-powershell-prompt-with-psreadline
if ($host.Name -eq 'ConsoleHost') {
    Import-Module PSReadLine
}
Set-PSReadLineKeyHandler -Key UpArrow -Function HistorySearchBackward
Set-PSReadLineKeyHandler -Key DownArrow -Function HistorySearchForward

# Must come after posh-git (https://github.com/vors/ZLocation)
Import-Module ZLocation

# https://ohmyposh.dev/docs/windows
Set-PoshPrompt Agnoster