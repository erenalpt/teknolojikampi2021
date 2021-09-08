import apt

def installedPackages():
	print(list(pkg.name for pkg in cache if pkg.is_installed))

installedPackages()
