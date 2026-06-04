from pathlib import Path

from sqlalchemy.dialects import mssql
from sqlalchemy.schema import CreateTable

from models.registry import MODEL_REGISTRY


ddl_lines = []

for model in MODEL_REGISTRY.values():
    ddl_lines.append(
        str(
            CreateTable(model.__table__).compile(
                dialect=mssql.dialect()
            )
        )
    )
    ddl_lines.append("GO\n")

output_file = Path("generated_schema.sql")

output_file.write_text(
    "\n".join(ddl_lines),
    encoding="utf-8",
)

print(f"DDL written to {output_file.resolve()}")