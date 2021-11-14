## Generate models
gen:
	@poetry run python -m codegen && \
	poetry run black vkmodels > /dev/null && \
	poetry run isort vkmodels > /dev/null