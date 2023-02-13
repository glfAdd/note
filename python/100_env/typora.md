##### 调整Typora书写区域为自适应宽度

```
打开Typora——>文件——>偏好设置——>外观——>打开主题文件夹——>打开github.css（默认使用的这个主题，若换了主题则打开对应的文件）
```

修改下面内容

```
#write {
    max-width: 4000px;
  	margin: 0 auto;
  	padding: 30px;
    padding-bottom: 100px;
}

@media only screen and (min-width: 1400px) {
	#write {
		max-width: 1400px;
	}
}

@media only screen and (min-width: 1800px) {
	#write {
		max-width: 1800px;
	}
}
```

