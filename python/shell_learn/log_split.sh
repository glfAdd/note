#! /bin/sh
file_path=/logs;
file_name=ndc_data_pro.log;
t=$(date -d now +%Y%m%d);
new_file_name=$file_name.$t;
cd $file_path && cp $file_name $new_file_name;
cat /dev/null > $file_name;