import apt

print(list(pkg.name for pkg in cache if pkg.is_installed))