import pymysql
import copy
from resources.rdbresource import get_by_by_query
from graphs.got.got_graph import GotGraph

graph = GotGraph()

def get_characters_by_query(args):
    res = get_by_by_query("HW4GoT", "characters", args)
    return res

def get_character_by_id(ch_id):
    args = {"character_id": ch_id.upper()}
    res = get_by_by_query("HW4GoT", "characters", args)
    return res

def get_related_characters(ch_id, r_kind):
    ch_id, r_kind = ch_id.upper(), r_kind.upper()
    res = graph.get_related_characters(ch_id, r_kind)
    ret = []
    for r in res:
        d = dict(r.end_node)
        if d["character_id"] != ch_id:
            ret.append(d)
    return ret
