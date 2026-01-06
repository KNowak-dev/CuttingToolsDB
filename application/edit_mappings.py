from edit_tool import EditOption

EDIT_OPTION_TO_FIELD_MAP:dict[EditOption, str] = {EditOption.TYPE_TOOL: "type_tool",
                                                EditOption.ORIGIN: "origin",
                                                EditOption.NR_EDV_SEMI_FINISHED_PRODUCT: "nr_edv_semi_finished_product",
                                                EditOption.KIND_TOOL: "kind_tool",
                                                EditOption.PRODUCTION_DETAIL: "production_detail",
                                                EditOption.MACHINE: "machine",
                                                EditOption.PRODUCTION_MACHINE: "production_machine",
                                                EditOption.SEMI_FINISHED_PRODUCT_PRICE: "semi_finished_product_price",
                                                EditOption.TOTAL_PRICE: "total_price",
                                                EditOption.COATING: "coating"
                                                }

if __name__ == "__main__":
    pass
        