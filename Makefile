## Generate models
gen:
	@poetry run python -m codegen && \
	poetry run black vkmodels > /dev/null && \
	poetry run isort vkmodels > /dev/null;

style:
	poetry run black codegen > /dev/null && \
	poetry run isort codegen > /dev/null;