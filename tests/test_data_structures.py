from app.data_structures import SegmentTree, Trie, UnionFind


def test_trie_prefix() -> None:
    trie = Trie()
    trie.insert("Library")
    trie.insert("Lab")
    assert "lib" in trie.search_prefix("Lib")


def test_union_find() -> None:
    uf = UnionFind(["a", "b", "c"])
    uf.union("a", "b")
    assert uf.find("a") == uf.find("b")
    assert uf.find("a") != uf.find("c")


def test_segment_tree() -> None:
    tree = SegmentTree([1, 2, 3, 4, 5])
    assert tree.range_sum(1, 4) == 9
