import pandas as pd

# Load the data
purchase_orders = pd.read_excel('files_for_container/erp_data/tabPurchase Order.xlsx')
purchase_order_items = pd.read_excel('files_for_container/erp_data/tabPurchase Order Item.xlsx')
purchase_receipts = pd.read_excel('files_for_container/erp_data/tabPurchase Receipt.xlsx')
purchase_receipt_items = pd.read_excel('files_for_container/erp_data/tabPurchase Receipt Item.xlsx')


# Join the data
flattable = pd.merge(
    purchase_orders, 
    purchase_order_items, 
    how='left',
    left_on = 'name',
    right_on = 'parent',
    suffixes = ('_po', '_po_items')
    )


flattable = pd.merge( 
    flattable, 
    purchase_receipt_items, 
    how='left',
    left_on = 'name_po',
    right_on = 'purchase_order',
    suffixes = ('', '_receipt_items')
    )

flattable = pd.merge( 
        flattable, 
        purchase_receipts, 
        how='left',
        left_on = 'parent_receipt_items',
        right_on = 'name',
        suffixes = ('', '_receipt')
        )    


flattable.shape

flattable["days_late"] = flattable["posting_date"] - flattable["schedule_date_po"]

flattable["days_late_number"] = flattable["days_late"].dt.days


flattable["late"] = flattable["posting_date"] > flattable["schedule_date_po"]