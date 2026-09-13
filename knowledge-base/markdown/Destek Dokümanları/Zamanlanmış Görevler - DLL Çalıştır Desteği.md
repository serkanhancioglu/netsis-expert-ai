---
title: "Zamanlanmış Görevler - DLL Çalıştır Desteği"
page_id: "153158632"
product: "netsis-3-enterprise"
depth: 2
is_section: false
is_stub: false
breadcrumb:
  - "Logo Netsis 3 Enterprise Bilgi Deposu"
  - "Destek Dokümanları"
  - "Zamanlanmış Görevler - DLL Çalıştır Desteği"
breadcrumb_path: "Logo Netsis 3 Enterprise Bilgi Deposu / Destek Dokümanları / Zamanlanmış Görevler - DLL Çalıştır Desteği"
source_url: "https://polaris.logo.cloud/docs/netsis-3-enterprise/detail/ZXh0ZXJuYWw_Y2lkPTAzYWJlOTVhLWNlYjktNDBkMi04ZTkzLTllYWVmYmUxMWZhYSZsaW5rPTUwYWI5YmMxLThhOWMtNDg5ZS1hZmUzLTVmYmZmNTU4ZmFiMCZ0ZW5hbnRJZD1jZGQ4N2UxMy0zMDA5LTRkZDEtYTViOC0yYTAwNWMwZTU4ZGEmaGlkZU5hbWU9VHJ1ZQ"
doc_url: "external?cid=03abe95a-ceb9-40d2-8e93-9eaefbe11faa&link=50ab9bc1-8a9c-489e-afe3-5fbff558fab0&tenantId=cdd87e13-3009-4dd1-a5b8-2a005c0e58da&hideName=True"
slug: "zamanlanmis-gorevler-dll-calistir-destegi_153158647_153158632.html"
source_version: "2024-10-11T14:29:37.990+03:00"
source_bytes: 998000
fetched_at: "2026-09-13T04:22:35+00:00"
generator: "netsis-scraper 1.0.0"
---
# Zamanlanmış Görevler - DLL Çalıştır Desteği

Zamanlanmış Görevler eklentisinde "DLL Çalıştır" desteği ile özel olarak oluşturulan DLL dosyaları eklenti üzerinde çalıştırılabilmektedir.

Bu özellik Netsis 3 Enterprise ve Netsis Wings Enterprise paketlerinde desteklenmektedir. Özelliğin kullanılabilmesi için Netsis sürümü 9.0.34 veya üzeri olmalıdır.

Visual Studio'da C# ile oluşturulan projelerde "…\\Netsis\\ENTERPRISE9\\Kurulum\\Utilities\\Zamanlanmis Gorevler Template" dizininde bulunan "Netsis Scheduler Custom Task.zip" .Net Template kullanılmalıdır.

![](../_assets/4c22b6b1638b3d568de5.png)

Proje oluşturmadan önce "Netsis Scheduler Custom Task.zip" dosyası "C:\\Users\\...\\Documents\\Visual Studio {version}\\Templates\\ProjectTemplates" klasörüne kopyalanmalıdır.

![](../_assets/dbd9c9240663815a6f08.png)

Create a new project menüsünden arama alanına "Netsis" yazılarak "Netsis Scheduler Custom Task" seçilerek yeni proje oluşturulabilir.

![](../_assets/0c5c9a719fb5a5125818.png)

![](../_assets/8597d88aa79f0dec987c.png)![](../_assets/bed5bb9618db78da9a1f.png)

**Run** **Metodu:** Zamanlanmış görev çalıştığı esnada gerçekleşmesi istenen işlemlerin yazılacağı ana metottur.

**TaskParamList:** Zamanlanmış görev parametreleri için tanımlanmış listedir.

Görev tanımı sırasında belirli parametrelerin arayüzden seçim yapılması için oluşturulan listeye eklenmesi gerekir. Eklenen parametreler Zamanlanmış Görev Tanımı ekranında DLL seçimi sonrasında "Parametreler" alanında listelenmektedir.

![](../_assets/e0dac9d8de55057c6f35.png)

Aşağıdaki örnek NetOpenX ile Yaşlandırmalı Özel Hesap Kapatma işleminin DLL üzerinden zamanlanmış görevler eklentisinde çalıştırılması için proje kodlarını içermektedir.

Derleme tamamlandığında DLL dosyaları "…\\Netsis\\ENTERPRISE9\\TemelSet\\OzelDLL" dizininde proje adı ile aynı adı sahip bir klasör oluşturularak içine kopyalanmalıdır. Bu işlem sonrasında zamanlanmış görevler eklentisinde görev tipi DLL Çalıştır seçeneği işaretlendiğinde DLL Seçimi alanında, oluşturulan DLL dosyaların seçimi yapılabilecektir.

using NetOpenX50;
namespace Netsis.CustumDllTask
{

public class CustomTask : ICustomTaskExecuter
{

private object yaslandirma;
public List\<Taskflaram\> TaskflaramList { get; set; }

public CustomTask()

{

TaskflaramList = new List\<Taskflaram\>();

flarameter();

}
private void Addflaram(string Akey, string AValue, TaskflaramValueType AvalueType =

TaskflaramValueType.valVariant, string ADescription = "", Boolean aEnabled = true, List\<DefaultflaramValue\>

flDefaultValues = null)

{

Taskflaram tmpTaskflaram = new Taskflaram();

tmpTaskflaram.KEY = Akey;

tmpTaskflaram.VALUE = AValue;

tmpTaskflaram.VALUETYPE = AvalueType;

tmpTaskflaram.DESCRIPTION = ADescription;

tmpTaskflaram.ENABLED = aEnabled;
tmpTaskflaram.DEFFAULTVALUELIST = flDefaultValues;

TaskflaramList.Add(tmpTaskflaram);

}
private void flarameter()
{

Addflaram("Cari Kodu", "", TaskflaramValueType.valstring, "Cari Kodu");

}
public ITaskExecuteResult Run(ITaskSettings pTaskSettings)
{

TaskExecuteResult tmpTaskResult = new TaskExecuteResult();

Kernel kernel = new Kernel();
Sirket sirket = default(Sirket);

try

{

string cariKodu = pTaskSettings.flARAMS.Find(x =\> x.KEY == "Cari Kodu").VALUE;
Yaslandirma yaslandirma = default(Yaslandirma);
sirket = kernel.yeniSirket(TVTTipi .vtMSSǪL, "companyName", "TEMELSET", "", "userName", "password", 0);

yaslandirma = kernel.yen Yaslandirma(sirket);
yaslandirma.Cari Kod = cari Kodu.ToString();

yaslandirma.Calistir();
return tmpTaskResult;

}
catch (Exception ex)

{

tmpTaskResult.ExecuterEx = ex;

tmpTaskResult.Status = CodeExecuteStatus.Error;
File.WriteAllText(@"C:\\Netsis\\ENTERPRISE9\\TemelSet\\OzelDLL\\OzelHesapKapatma\\Log\\ErrorLog.txt",

ex.Message.ToString());

return tmpTaskResult;
}
finally

{

Marshal.ReleaseComObject(yaslandirma);

Marshal.ReleaseComObject(sirket);

kernel.FreeNetsisLibrary();

Marshal.ReleaseComObject(kernel);

}

}

}

}

![](../_assets/3d3464557b49fd51af55.png)

Aşağıdaki örnek SQL Server Management Objects (SMO) kütüphanesi kullanılarak database backup işlemlerinin zamanlanmış görevler eklentisi üzerinden DLL ile gerçekleştirilmesi için oluşturulmuştur.

Projede SMO referansı için Microsoft.SqlServer.SqlManagementObjects paketi ve Microsoft.SqlServer.Management.Smo namespece'i eklenmiştir. *"using* *Microsoft.SqlServer.Management.Smo;"*

public CustomTask()
{

TaskflaramList = new List\<Taskflaram\>();
Addflaram("Text", "", TaskflaramValueType.valstring, "Veritabanı Adı");
}

public ITaskExecuteResult Run(ITaskSettings pTaskSettings)
{

TaskExecuteResult tmpTaskResult = new TaskExecuteResult();

try
{

string tmpDatabaseName = pTaskSettings.flARAMS.Find(x =\> x.KEY == "Text").VALUE;

string backupFileName = $"{tmpDatabaseName}\_{DateTime.Now:ddMMyyyy}.bak";
Server srv = new Server(@"ServerName");

srv.ConnectionContext.LoginSecure = false;

srv.ConnectionContext.Login = "userName";

srv.ConnectionContext.flassword = "password";

Backup bckp = new Backup();

bckp.Database = tmpDatabaseName;
bckp.Devices.AddDevice(@"C:\\Backups\\" + backupFileName, DeviceType.File);

bckp.Action = BackupActionType.Database;
bckp.Initialize = true;

bckp.SqlBackup(srv);

return tmpTaskResult;

}

catch (Exception ex)

{
tmpTaskResult.ExecuterEx = ex;

tmpTaskResult.Status = CodeExecuteStatus.Error;
File.WriteAllText(@"C:\\Netsis\\ENTERPRISE9\\TemelSet\\OzelDLL\\DatabaseBackup\\Log\\ErrorLog.txt",

ex.Message.ToString());

return tmpTaskResult;

} ;

}
