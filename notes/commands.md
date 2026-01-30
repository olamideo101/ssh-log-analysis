# SSH Analysis Commands

## Check SSH service status
systemctl status ssh

## View authentication logs
sudo cat /var/log/auth.log

## Filter failed SSH login attempts
sudo grep "Failed password" /var/log/auth.log

## Review SSH daemon configuration
sudo nano /etc/ssh/sshd_config
