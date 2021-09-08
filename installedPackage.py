import apt

def installedPackage(packagesName):
	cache = apt.Cache()
	print("True" if (packagesNamelist in (pkg.name for pkg in cache if pkg.is_installed)) else "False")

installedPackage("liman")