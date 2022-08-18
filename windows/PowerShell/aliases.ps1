

# directory navigation
function .. { Set-Location .. }
function ... { Set-Location .. ; Set-Location .. }
function .... { Set-Location .. ; Set-Location .. ; Set-Location .. }
function ..... { Set-Location .. ; Set-Location .. ; Set-Location .. ; Set-Location .. }
function home { Set-Location $env:USERPROFILE }

# Git aliases
function ggs { git status }
function gga($file) { git add $file }
function ggai { git add --interactive }
function ggaa { git add --all }
function ggc($msg) { if ($msg) { git commit -m $msg } else { git commit } }
function ggca { git commit --amend }
function ggcaa { git commit --amend --no-edit }
function ggp { git push }
function ggpf { git push --force-with-lease }
function ggu { git pull --ff-only }
function ggd { git diff }
function ggds { git diff --staged }
function ggl { git log --graph --color --all --decorate --format="%C(auto)%d %s" }
function ggll { git log --graph --color --all --decorate --format="%C(auto)%h %d %s %Cblue %ar %an" }
function ggx { git show -s --format='%Cgreen%h %Cblue%an %Cred%cr%Creset%n%s' }
function ggroot { Push-Location (git rev-parse --show-toplevel) }

# Helper functions
function Time-Execution ($command) {
    Measure-Command { $command }
}

# Docker functions
function Start-Ansible {
    # docker run --rm -it -v ${PWD}:/play ansible/ansible-runner:latest bash
    docker run --rm -it -v ${PWD}:/play -v ${HOME}/.ssh:/root/ssh ansible/ansible-runner:latest bash
}