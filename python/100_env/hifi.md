##### SD 卡格式化

```shell
# 查看磁盘列表
$ diskutil list
# 卸载 U 盘
$ diskutil unmountDisk /dev/disk4
# 格式化 U 盘
$ diskutil eraseDisk FAT32 USBNAME MBRFormat /dev/disk4
```

