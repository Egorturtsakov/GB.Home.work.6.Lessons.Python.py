def parse_log(pth_file):

    if pth_file:
        with open(pth_file,"r",encoding="utf-8") as file:
            for line in file:
                ip = line.split(" - - ")[0]
                rsp_and_pth = line.split('"')[1]
                rsp = rsp_and_pth.split()[0]
                pth = rsp_and_pth.split()[1]
                yield(ip, rsp, pth)


def find_spamer(parsed_log):
    pass



if __name__ == "__main__":
   a = parse_log("./nginx_logs.txt")
   for e in a:
       print(e)