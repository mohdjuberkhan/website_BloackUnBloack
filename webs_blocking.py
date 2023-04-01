def block_site(website):
        web=website
        website=redirect+' '+website+'\n'
        with open (host_path,"r+") as host_file :
                content=host_file.readlines()
                if website in content:
                        print(f'*********************  "{web}" already block')
                else:
                        host_file.write(website)
                        print(f'\n**********************  "{web}"  succussfully blocked')
def unblock_site():
        with open(host_path,'r+') as host_file:
                content=host_file.readlines()
                contentEnum=enumerate(content)
                if len(content)!=0:
                        while True:
                                print('Blocked sites are: \n')
                                for i in contentEnum:
                                        print('\t',i)
                                ch=input('enter choic : ')
                                if ch.isnumeric():
                                        print(f"UNBLOCKED  '{content[int(ch)]}'")
                                        content.pop(int(ch))
                                        break
                                else:
                                        print('************************* please enter correct index number')
                else:
                        print('******************not a single site block here')
                        return
                       
        with open (host_path,'r+') as host_file:
                host_file.truncate()
        with open (host_path,'r+') as host_file:
                for i in set(content):
                        host_file.write(i)
               
if __name__=='__main__':
        host_path="C:/Windows/System32/drivers/etc/hosts"
        redirect="127.0.0.1"
        while True:
                while True:
                        print('\nwhat you want : \n1 : Block a site\n2 : Unblock a site\n3 : Exit\nPlease choose an option : ')
                        ch=input()
                        if ch.isnumeric():
                                break
                        print('\n************************please enter numeric value')
        
                if int(ch) == 1:
                        block_site(input('Enter site : '))
                elif int(ch) == 2:
                        unblock_site()
                elif int(ch) == 3:
                        exit()
                else:
                        print('incorrect option , please try again.')
        
