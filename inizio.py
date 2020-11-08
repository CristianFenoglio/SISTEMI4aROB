print("hello world")
#void OrdinaVettBubble(int v[], int n){
#	int k;
#	int t;
#	int i;
#	int pos=n;
#	while (pos!=1){
#        i=0;
#		for (k=0; k<pos-1;k++){
#			if (v[i]>v[i+1]){
#				t=v[i+1];
#				v[i+1]=v[i];
#				v[i]=t;
#			}
#			i++;
#		}
#		pos--;
#	}
#}
def bubble(list):
    i=0
    pos=len(list)
    while pos!=1:
        for t in range (len(list)):
            if(list[i]<list[t]):
                temp=list[i]
                list[i]=list[t]
                list[t]=temp
            i=i+1
        pos=pos-1
    return list



