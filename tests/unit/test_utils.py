import logging

from fastapi.testclient import TestClient
from app.utils.prefixes.prefix_utils import remap_prefixes
from app.main import app
from prefixmaps import load_context
from curies import Converter
test_client = TestClient(app)

logger = logging.getLogger(__name__)

gene_ids = ["ZFIN:ZDB-GENE-980526-388", "ZFIN:ZDB-GENE-990415-8"]
go_ids = ["GO:0008150"]
subsets = ["goslim_agr"]
shared_ancestors = [("GO:0006259", "GO:0046483")]


def test_prefix_utils():
    context = load_context("go")
    extended_prefix_map = context.as_extended_prefix_map()
    converter = Converter.from_extended_prefix_map(extended_prefix_map)
    cmaps = converter.prefix_map
    # hacky solution to: https://github.com/geneontology/go-site/issues/2000
    cmaps = remap_prefixes(cmaps)
    assert(cmaps["MGI"] == "http://identifiers.org/mgi/MGI:")
