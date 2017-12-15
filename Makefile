all: example.py.png
	echo done

%.cov: %.py
	python3 pycfg/branchcov.py $*.py main '1+1+10' 2> $*.cov_
	mv $*.cov_ $*.cov

%.py.png: %.cov
	python3 pycfg/pycfg.py $*.py -d -y $*.cov 2> $*.dot

clean:
	rm -f *.cov *.png *.dot
	rm -rf __pycache__
