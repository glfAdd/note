product_type = ['air', 'train', 'hotel']
provider_id = [1, 2, 3, 4]
invoice_classification = [1, 2, 3, 4, 5, 6]
invoice_type = [1, 2, 3, 4]
domestic_and_international = [1, 2]
internal_and_external = [1, 2]
aa = []
# , , , order_invoice_conf_id, service_invoice_conf_id, refund_invoice_conf_id, tenant_id, domestic_and_international, internal_and_external, creator, updater, deleted
for p1 in product_type:
    for p2 in provider_id:
        for i1 in invoice_classification:
            for i2 in invoice_type:
                for d in domestic_and_international:
                    for i3 in internal_and_external:
                        aa.append([525, p1, p2, 1, 1, 1, 2, 1, 1, 113961, 113961, 00])
print(aa)
