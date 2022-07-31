# See LICENSE.vyoma for details

TOPLEVEL_LANG ?= verilog

PWD=$(shell pwd)

VERILOG_SOURCES = $(PWD)/round_robin_arbiter_buggy.v               # provide your design path

TOPLEVEL := round_robin_arbiter          # design file
MODULE   := test_arbiter    # test file

include $(shell cocotb-config --makefiles)/Makefile.sim

clean_all: clean
	rm -rf *.xml sim_build __pycache__ 
