class Solution:
    def subdomainVisits(self, cpdomains: list[str]) -> list[str]:
        map = {}
        arr = []

        for input in cpdomains:
            count_domain = input.split() # default is space - splits into count & domain
            count = int(count_domain[0])
            domain = count_domain[1]

            domain_split = domain.split(".") # ["discuss", "leetcode", "com"]

            for i in range(len(domain_split)):
                subdomain = domain_split[i]
                for j in range(i+1, len(domain_split)):
                    subdomain += "." + domain_split[j]
                
                print(subdomain)
                if subdomain not in map:
                    map[subdomain] = count
                else:
                    map[subdomain] += count
         
        for key, value in map.items():
            arr.append(str(value) + " " + key)

        return arr