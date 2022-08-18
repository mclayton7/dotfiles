# https://stackoverflow.com/questions/52017316/how-to-add-all-projects-to-a-single-solution-with-dotnet-sln
function Create-Solution {
    $projects = Get-ChildItem -Recurse | Where-Object { $_.Name -match '^.+\.(csproj|vbproj)$' }

    $uniqueProjects = $projects | Group-Object -Property Name | Where-Object Count -EQ 1 | Select-Object -ExpandProperty Group | ForEach-Object { $_.FullName }

    Invoke-Expression -Command "dotnet new sln"

    $uniqueProjects | ForEach-Object { Invoke-Expression -Command "dotnet sln add ""$_""" }
}