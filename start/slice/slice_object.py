class Group:
    # 支持切片操作
    def __init__(self, group_name, company_name, staffs):
        self.gropu_name = group_name
        self.company_name = company_name
        self.staffs = staffs

    def __reversed__(self):
        self.staffs.reverse()
    def __getitem__(self, item):
        cls = type(self)
        if isinstance(item, slice):
            return cls(group_name = self.gropu_name, company_name = self.company_name, staffs = self.staffs[item])
        else:
            return cls(group_name = self.gropu_name, company_name = self.company_name, staffs = [self.staffs[item]])
    def __len__(self):
        return len(self.staffs)
    def __iter__(self):
        return iter(self.staffs)
    def __contains__(self, item):
        if item in self.staffs:
            return True
        else:
            return False
staffs = ["bobby1", "imooc", "bobby2", "bobby3"]
group = Group(company_name="imooc", group_name = "user", staffs=staffs)
reversed(group)
sub_group = group[:2]
sub_group2 = group[0]
print(sub_group)
print(sub_group2)
print(len(group))
if "bobby1" in group:
    print("__contains__")
for user in group:
    print(user)
pass



