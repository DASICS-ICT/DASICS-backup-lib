for i in `find ./ -name "*.o"`
do
	echo ${i} 
	riscv64-unknown-linux-gnu-objcopy --weaken --rename-section .text=.ulibtext ${i}

done
