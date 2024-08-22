import os
import shutil
import subprocess

cache_size = [8, 16, 32, 64, 128, 256, 512]
L1_D_Associativity = [1,8]
L1_I_Associativity = [1,8]
L2_Associativity = [1,8]
L1_D_cache=[1, 8, 16, 32, 64, 128]
L1_I_cache=[1, 8, 16, 32, 64, 128]
L2_cache=[1, 8, 16, 32, 64, 128]

benchmark = "/home/011/k/kx/kxr230001/CA_Project_2/Project1_SPEC-master/456.hmmer"
cpu_type = "timing"

for size in cache_size:
	for L1_D_Assoc in L1_D_Associativity:
		for L1_I_Assoc in L1_I_Associativity:
			for L2_Assoc in L2_Associativity:
				for L1_D in L1_D_cache:
					for L1_I in L1_I_cache:
						for L2 in L2_cache:
							os.chdir("/home/011/k/kx/kxr230001/CA_Project_2/Output/456.hmmer/")
							dirname ="456#"+str(size)+"-"+str(L1_D_Assoc)+"-"+str(L1_I_Assoc)+"-"+str(L2_Assoc)+"-"+str(L1_D)+"-"+str(L1_I)+"-"+str(L2)
							if(os.path.isdir(dirname)):
								shutil.rmtree(dirname)

							os.makedirs(dirname)
							os.chdir("/usr/local/gem5")
							gem5_cmd = "./build/X86/gem5.opt -d /home/011/k/kx/kxr230001/CA_Project_2/Output/456.hmmer/"+dirname+"/ ./configs/example/se.py -c"+benchmark+"/src/benchmark -o "+benchmark+"/data/bombesin.hmm -I 50000000 --cpu-type="+cpu_type+" --caches --l2cache --l1d_size="+str(L1_D)+"kB --l1i_size="+str(L1_I)+"kB --l2_size="+str(L2)+"kB --l1d_assoc="+str(L1_D_Assoc)+" --l1i_assoc="+str(L1_I_Assoc)+" --l2_assoc="+str(L2_Assoc)+" --cacheline_size="+str(size)
							os.system(gem5_cmd)


