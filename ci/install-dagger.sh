#!/bin/sh
set -eu
# GitHub-hosted Linux amd64 bootstrap. Local users can use Dagger's official installer.
[ "$(uname -s)" = Linux ] && [ "$(uname -m)" = x86_64 ] || { echo 'This bootstrap targets Linux amd64.' >&2; exit 1; }
task_tmp_dir=$(mktemp -d)
trap 'rm -rf "$task_tmp_dir"' EXIT
curl --fail --silent --show-error --location https://dl.dagger.io/dagger/releases/1.0.0-beta.21/dagger_v1.0.0-beta.21_linux_amd64.tar.gz --output "$task_tmp_dir/dagger.tar.gz"
printf '%s  %s\n' 'c5ac777a5c99089869660943381136e22177b59a46412e310c2fef594760a041' "$task_tmp_dir/dagger.tar.gz" | sha256sum --check --status
tar -xzf "$task_tmp_dir/dagger.tar.gz" -C "$task_tmp_dir" dagger
install -m 755 "$task_tmp_dir/dagger" /usr/local/bin/dagger
