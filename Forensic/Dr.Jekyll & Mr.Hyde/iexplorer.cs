using System;
using System.Diagnostics;
namespace Explorer{
	class Program{
		static void Main(){
			Process proc = new Process();
			ProcessStartInfo procInfo = new ProcessStartInfo("powershell.exe");
			procInfo.CreateNoWindow = true;
			proc.StartInfo = procInfo;
			proc.Start();
		}
	}
}
