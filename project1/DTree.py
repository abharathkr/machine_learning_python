import math

class DTree(object):
    def __init__(self):
        self.attribute = None;
        self.Anum = None;
        self.child = []
        self.child_value = [];
                
    def printa (self):
        return self.attribute;
        
    def insert_child_value(self,a):
        self.child_value.append(a);

    def insert_value(self, a, b):
        self.attribute = a;
        self.Anum = b;
        
    def insert_child(self, m):
        self.child.append(m);
        
    def display (self):
        print(self.attribute);
        print(self.child_value)
        if self.child != []:
            for j in range (len(self.child)):
                print (self.child[j].printa());
                
        if self.child != []:
            for j in range(len(self.child)):
                self.child[j].display();
    
def create_matrix (file):
    with open(file) as textFile:
        mat = [line.split(",") for line in textFile];
    return mat
    
def create_submatrix (mat, att_value, att_num):  
    sub_mat = [];
    l = len(mat);
    for i in range (l):
        if mat[i][att_num] == att_value :
            newr = mat[i];
            sub_mat.append(newr);
    return sub_mat
    
def entropy_after (mat, anum, flag):
    """ array to store entropy of the 22 attributes"""
    entropy = [];
    """array to maintain count of number of rows with p"""
    cp = [];
    """array to maintain count of number of rows with e"""
    ce = [];
    
    eb = entropy_before(mat);
    
    tlen = len(mat);
    for i in range (len(anum)):
        if flag[i] == 1:
            cp.append([eb]);
            ce.append([eb]);
            entropy.append(eb);
            continue;
        p = [];
        e = [];
        for k in range (len(anum[i])):
            t1 = 0;
            t2 = 0;
            for j in  range (tlen):
                if mat[j][i] == anum[i][k] and mat[j][0] == 'p' :
                    t1 = t1 + 1;
                elif mat[j][i] == anum[i][k] and mat[j][0]!= 'p' :
                    t2 = t2 + 1;
            p.append(t1);
            e.append(t2);
        cp.append(p);
        print(cp);
        ce.append(e); 
        print(ce);
        temp = 0;
        for j in range (len(anum[i])):
            if cp[i][j] == 0:
                continue;  
            a = (cp[i][j])/float(cp[i][j]+ce[i][j]);
            print(a);
            temp = temp +(float(cp[i][j]+ce[i][j])/len(mat))*(-1*a*math.log(a,2));  
            print(temp);
        entropy.append(temp);
        
        
    print (entropy);
    return entropy;
    
def entropy_before(mat):
    length_mat = len(mat);
    poison_c = 0;
    edible_c = 0;
    for i in range(len(mat)):
        if mat[i][0] == 'p':
            poison_c += 1;  
        elif mat[i][0] == 'e':
            edible_c += 1;
    
    if poison_c == 0:
        entropy_value = -(edible_c/float(length_mat))*(math.log((edible_c/float(length_mat)),2));
        return entropy_value
    if edible_c == 0:
        entropy_value = -((poison_c/float(length_mat))*math.log((poison_c/float(length_mat)),2));
        return entropy_value
    entropy_value = -((poison_c/float(length_mat))*math.log((poison_c/float(length_mat)),2))-(edible_c/float(length_mat))*(math.log((edible_c/float(length_mat)),2))
    return entropy_value
    
def gain_calc(mat,a_list,flag):
    eA = entropy_after(mat,a_list,flag)
    eB = entropy_before(mat);
    gain = [];
    for i in range(len(a_list)):
        g = eB - eA[i]
        gain.append(g);
    max_gain = 0.0;
    print(gain);
    k = 0;
    for i in range(0,len(gain)):
        if max_gain < gain[i]:
            max_gain = gain[i]
            k = i;
    return k;  
    
def countp (mat):
    count  = 0;
    for i in range (len(mat)):
        if mat[i][0] == 'p' :
            count = count + 1;  
            
    return count;
    
def counte (mat):
    count  = 0;
    for i in range (len(mat)):
        if mat[i][0] == 'e':
            count = count + 1;
            
    return count;
    
def mis_classification (mat, a_list, flag,mce):
    maxta = [];
    for i in range (len(a_list)):
        maxv = 0;
        if flag[i] == 1:
           maxta.append(-100); 
           continue;
        for k in range (len(a_list[i])):
            tempe = 0;
            tempp = 0;
            for j in range(len(mat)):
                if mat[j][i] == a_list[i][k] and m[j][0] == 'p':
                    tempp = tempp + 1;
                if mat[j][i] == a_list[i][k] and mat[j][0] == 'e':
                    tempe = tempe + 1
            if (tempp+tempe) == 0:
                continue;
            pp = float(tempp)/(tempp+tempe);
            pe = float(tempe)/(tempp+tempe);
            a = [pp,pe];
            print(max(a));
            temp = ((1-max(a))*(float(tempp+tempe)/len(mat)));
            print(temp);
            maxv = maxv +  temp;
        maxv = mce - maxv;
        maxta.append(maxv);    
    print(maxta);
    minr = -100;
    for i in range (len(maxta)):
        if minr < maxta[i]:
            minr = maxta[i];
            mini = i;
            
    print (mini);
    return mini;
     
def split (mat,alist,node,anum_v,flag,mce):
    g = mis_classification(mat,alist,flag,mce);
    print(g);
    tmat = mat;
    flag[g] = 1;
    node.insert_value(anum_v[g],g);
    temp_list = alist[g];
    index = anum[g];
    tflag = flag;
    for j in range (len(temp_list)):
        print(j)
        m = create_submatrix(tmat,temp_list[j],index)
        print(m)
        print(len(m));
        if counte(m) == len(m):
            n  = DTree();
            n.insert_value('e',None);
            node.insert_child_value([temp_list[j]]);
            node.insert_child(n);
            continue
        if countp(m) == len(m):
            n = DTree();
            n.insert_value('p',None);
            node.insert_child_value([temp_list[j]]);
            node.insert_child(n);
            continue
        if len(alist) == 0:
            continue
        child_node = DTree();
        node.insert_child(child_node);
        node.insert_child_value([temp_list[j]]);
        p = countp(m);
        e = counte(m);
        pp = float(p)/(p+e);
        pe = 1-pp;
        a = [pp,pe];
        print(pp);
        print(pe);
        mce = 1 - max(a);
        split(m,alist,child_node,anum_v,tflag,mce);    
    return
node = DTree();    
m = create_matrix("training.txt");
anum = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22];
alist = [['p','e'],['b','c','x','f','k','s'],['f','g','y','s'],['n','b','c','g','r','p','u','e','w','y','t','f'],['t','f'],['a','l','c','y','f','m','n','p','s'],['a','d','f','n'],['c','w','d'],['b','n'],['k','n','b','h','g','r','o','p','u','e','w','y'],['e','t'],['b','c','u','e','z','r','?'],['f','y','k','s'],['f','y','k','s'],['n','b','c','g','o','p','e','w','y'],['n','b','c','g','o','p','e','w','y'],['p','u'],['n','o','w','y'],['n','o','t'],['c','e','f','l','n','p','s','z'],['k','n','b','h','r','o','u','w','y'],['a','c','n','s','v','y'],['g\n','l\n','m\n','p\n','u\n','w\n','d\n']];
flag = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0];
anum_v =  ['result','cap-shape','cap-surface','cap-color','bruises','odor','gill-attachment','gill-spacing','gill-size','gill-color','stalk-shape','stalk-root','stalk-surface-above-ring','stalk-surface-below-ring','stalk-color-above-ring','stalk-color-below-ring','veil-type','veil-color','ring-number','ring-type','spore-print-color','population','habitat'];
p = countp(m);
e = counte(m);
pp = float(p)/(p+e);
pe = 1-pp;
a = [pp,pe];
print(pp);
print(pe);
mce = 1 - max(a);
print(mce);
split (m,alist,node,anum_v,flag,mce);
node.display();