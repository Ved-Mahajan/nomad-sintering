from nomad.config.models.plugins import SchemaPackageEntryPoint
from pydantic import Field


class SinteringEntryPoint(SchemaPackageEntryPoint):
    parameter: int = Field(0, description='Custom configuration parameter')

    def load(self):
        from sintering.schema_packages.sintering import m_package

        return m_package


schema_package_entry_point = SinteringEntryPoint(
    name='Sintering',
    description='New schema package for describing a sintering process',
)
