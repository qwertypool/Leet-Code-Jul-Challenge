class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        if hour == 12:
            hour=0
        if minutes == 60:
            minutes = 0
            hour = hour + 1
        hour_angle = (hour*60 + minutes)*0.5
        minute_angle = minutes*6
        angle = abs(hour_angle - minute_angle)
        result = min(360-angle, angle)
        return result

