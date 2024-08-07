import requests
import json
import lxml.builder as builder
from acdh_tei_pyutils.tei import TeiReader

NewElement = builder.ElementMaker()

############ cfg #############
odd_path = "./odd/b-vg.odd"


class CFG:
    def __init__(
        self,
        source_json_url: str,
        type_column_name: str,
        targeted_element_name: str,
        targeted_attribute_name: str,
        type_description_field_name: str = "description",
        local_dump_copy_file=None,
    ):
        self.tageted_element_name = targeted_element_name
        self.targeted_attribute_name = targeted_attribute_name
        self.target_attDef_xpath=f"//tei:elementSpec[@ident='{targeted_element_name}']//tei:attDef[@ident='{targeted_attribute_name}']"
        self.source_json_url = source_json_url
        self.type_column_name = type_column_name
        self.type_description_field_name = type_description_field_name
        self.local_dump_copy_file = local_dump_copy_file


def fetch_metadata_json(
    url: str,
    local_filepath: str
) -> dict:
    print(f"downloading from {url}")
    results = requests.get(url)
    json_result = results.json()
    if local_filepath:
        with open(local_filepath, "w") as outfile:
            json.dump(json_result, outfile)
    return json_result


def get_valItems_from_json(cfg: CFG) -> list:
    dump_json = fetch_metadata_json(
        url=cfg.source_json_url,
        local_filepath=cfg.local_dump_copy_file
    )
    valItems = []
    for row in dump_json.values():
        value = row[cfg.type_column_name]
        description = row.get(cfg.type_description_field_name)
        description_text = description if description else value
        valItem = NewElement.valItem(
            "\n",
            NewElement.desc(description_text),
            "\n",
            ident=value
        )
        valItems.append(valItem)
    return valItems


def create_new_closed_valList(valItems: list):
    valList = NewElement.valList(type="closed")
    for valItem in valItems:
        valList.append(valItem)
    return valList


def write_values_to_closed_val_list(
    odd_doc: TeiReader,
    cfg: CFG,
    valItems: list
) -> None:
    # create new xml valList element
    new_closed_valList = create_new_closed_valList(valItems)
    print(f"writing {len(new_closed_valList)} entries to the '@{cfg.targeted_attribute_name}' attribute of '{cfg.tageted_element_name}'.")
    # get attDef element from odd
    try:
        attDef = odd_doc.any_xpath(cfg.target_attDef_xpath)[0]
    except IndexError as e:
        print(f"\nTrying to find attDef with xpath:\"{cfg.target_attDef_xpath}\" fails.\nDoes this element realy exist in your odd?\n")
        raise e
    # remove old closed valList if existing
    old_closed_valLists = odd_doc.any_xpath(
        f"{cfg.target_attDef_xpath}/tei:valList[@type='closed']"
    )
    if old_closed_valLists:
        for old_closed_valList in old_closed_valLists:
            attDef.remove(old_closed_valList)
    # add new list to the attDef
    attDef.append(new_closed_valList)


def write_json_vals_to_odd(odd_doc, cfg: CFG):
    valItems = get_valItems_from_json(cfg)
    write_values_to_closed_val_list(
        odd_doc,
        cfg,
        valItems
    )


odd_doc = TeiReader(odd_path)

if __name__ == "__main__":
    cfgs = [
        CFG(
            source_json_url="https://raw.githubusercontent.com/bundesverfassung-oesterreich/bv-entities/main/json_dumps/type_of_document.json",
            type_column_name="name",
            targeted_element_name="text",
            targeted_attribute_name="type",
            type_description_field_name="has_description",
        ),
        CFG(
            source_json_url="https://raw.githubusercontent.com/bundesverfassung-oesterreich/bv-entities/main/json_dumps/type_of_manifestation.json",
            type_column_name="name",
            targeted_element_name="objectDesc",
            targeted_attribute_name="form",
            type_description_field_name="has_description",
        ),
        CFG(
            source_json_url="https://raw.githubusercontent.com/bundesverfassung-oesterreich/bv-entities/main/json_dumps/xml_authors.json",
            type_column_name="shorthand",
            targeted_element_name="change",
            targeted_attribute_name="who",
            type_description_field_name="name"
        ),
        CFG(
            source_json_url="https://raw.githubusercontent.com/bundesverfassung-oesterreich/bv-entities/main/json_dumps/document.json",
            type_column_name="bv_id",
            targeted_element_name="witness",
            targeted_attribute_name="sameAs",
            type_description_field_name="doc_title"
        )
    ]
    for cfg in cfgs:
        write_json_vals_to_odd(odd_doc, cfg)
    odd_doc.tree_to_file(odd_doc.file)
    print(f"updated {odd_doc.file}")