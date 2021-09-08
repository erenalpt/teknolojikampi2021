import apt

def installedPackages():
	cache = apt.Cache()
	print(list(pkg.name for pkg in cache if pkg.is_installed))

installedPackages()
