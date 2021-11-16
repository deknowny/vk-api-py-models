import os
import pathlib
import shutil
import threading

import loguru
from codegen.generators.objects import ObjectsGenerator


def entrypoint():
    models_path = pathlib.Path("vkmodels")
    schema_path = pathlib.Path("vk-api-schema")
    codegen_path = pathlib.Path("codegen")

    loguru.logger.opt(colors=True).info(
        "Run codegen code <c>{codegen_dir}</c> "
        "from schema <c>{schema_dir}</c> to models <c>{models_dir}</c>",
        codegen_dir=codegen_path.stem,
        models_dir=models_path.stem,
        schema_dir=schema_path.stem,
    )

    shutil.rmtree(models_path, ignore_errors=True)
    models_path.mkdir()
    shutil.copytree(
        codegen_path / "templates" / "bases", models_path / "bases"
    )

    codegen = [
        ObjectsGenerator.fetch(
            models_path=models_path, schema_path=schema_path
        )
    ]

    codegen_threads = [
        threading.Thread(target=gen.run_codegen) for gen in codegen
    ]

    for thread in codegen_threads:
        thread.start()

    for thread in codegen_threads:
        thread.join()
