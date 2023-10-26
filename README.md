# booting-rohc
Yet another ROHC example with dockers.

## Motiviation
ROHC has been there for a long time, along with rich documentation in RFCs.
It also comes with examples on how to use ROHC [here](https://rohc-lib.org/presentation/getting-started/#learn-more), compressing a custom packet build in C language.
In addition, if you want to inspect the packet format after compressed, [there](https://github.com/didier-barvaux/rohc/tree/master/test) are also lots of pcap files available.

However, at least for me, the support is a bit niche. First, RFC documents are spread across different ones, while the base one, RFC 3095, is rather ill-organized and ambiguous in a way.
Thanks to the pcap they provided, I can get a better understanding on how it works by comparing the spec and implementations.

Then it followed with the second issue: I only find the "compressed" pcap, so there is no way for me to compare the packet before/after compression.
The "learn-more" guide they provided is also done in a very "networking" prospective. They build a packet in C language, which means you need to handle mostly everything just to construct 
a simple packet. For me, I don't care how to build a packet in C, I was here to learn how the compression/decompression is done. And they only do it in a monolith way, putting compression
and decompression in the same script.

Not that you can't observe the packet this way, but it is very weird to do so. Like, you want to know how the packet mutates in the ROHC workflow. 
Intuitively, one can setup several containers to simulate the workflow by tapping each interface, instead of running the whole stimulation in a script and in C (make your live suffer just to inspect the packet).

In short, I find the official "tutuorial" is kind of pushing people away from using it. Instead of teaching people how to use it, it is more likely trying to prove ROHC indeed works.
Fundamentally, you should always split the compressor and decompressor on different instances, since ROHC spend literally most of its effort on maintaining consistent contexts between these two entites.

## 