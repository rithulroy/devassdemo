"""A small greeting feature."""


def greet(name: str = "World") -> str:
	"""Return a friendly greeting for the supplied name."""
	name = name.strip()
	if not name:
		name = "World"
	return f"Hello, {name}!"


if __name__ == "__main__":
	print(greet())
