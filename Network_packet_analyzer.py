from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP, ICMP

def packet_callback(packet):
    """Processes and prints packet details."""
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = "Other"
        
        if packet.haslayer(TCP):
            protocol = "TCP"
        elif packet.haslayer(UDP):
            protocol = "UDP"
        elif packet.haslayer(ICMP):
            protocol = "ICMP"

        print(f"📡 {src_ip} → {dst_ip} | Protocol: {protocol}")
        
        # Print payload if available
        if packet.haslayer(TCP) or packet.haslayer(UDP):
            payload = bytes(packet[TCP].payload) if packet.haslayer(TCP) else bytes(packet[UDP].payload)
            if payload:
                print(f"   🔍 Payload: {payload[:50]}...")  # Show first 50 bytes for preview

def main():
    print("📡 Packet Sniffer Running... (Press Ctrl+C to stop)")
    sniff(prn=packet_callback, store=False)

if __name__ == "__main__":
    main()
