class laptop:
    def __init__(self,Name,processor,screensize,RAM,ROM,OS):
        self.Name=Name
        self.processor=processor
        self.screensize=screensize
        self.RAM=RAM
        self.ROM=ROM
        self.OS=OS
    def details(self):
        print("Name:",self.Name)
        print("Processor:",self.processor)
        print("Screen Size:",self.screensize)
        print("RAM:",self.RAM)
        print("ROM:",self.ROM)
        print("OS:",self.OS)
inst1=laptop("Dell","i5",15.6,"8GB","1TB","Windows 10")
inst2=laptop("HP","i7",14,"16GB","512GB","Windows 11")
inst3=laptop("Lenovo","i3",15.6,"4GB","1TB","Windows 10")
inst4=laptop("Asus","i5",14,"8GB","1TB","Windows 10")
inst5=laptop("Acer","i7",15.6,"16GB","512GB","Windows 11")
inst6=laptop("Apple","M1",13.3,"8GB","256GB","MacOS")
inst7=laptop("Microsoft","i5",13.5,"16GB","512GB","Windows 10")
inst8=laptop("Razer","i7",15.6,"32GB","1TB","Windows 10")
inst9=laptop("MSI","i9",17,"32GB","2TB","Windows 11")
inst10=laptop("Toshiba","i5",15.6,"8GB","1TB","Windows 10")
inst1.details()
inst2.details()
inst3.details()
inst4.details()
inst5.details()
inst6.details()
inst7.details()
inst8.details()
inst9.details()
inst10.details()